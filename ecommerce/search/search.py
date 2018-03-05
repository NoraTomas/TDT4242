from ..models import *
from simple_search import search_filter


def search_store(query={}):
    error = ''
    search_fields = ['^name', 'author__last_name', 'author__first_name']
    results = Item.objects.filter(search_filter(search_fields, query['query']))
    # if p_query['categories']:
    #     results.filter(category__in=query['categories'])
    #     pass
    results = filter_price(results, query['price_min'], query['price_max'])
    return results, error


def process_query(query):
    context = {'error': ''}
    p_query, error = preprocess_query(query)
    print(p_query)
    context['error'] += error
    items, error = search_store(p_query)
    print(p_query)
    context['error'] += error
    context['items'] = items
    context['query'] = p_query['query']
    context['price_min'] = p_query['price_min']
    context['price_max'] = p_query['price_max']
    print(context['price_min'], context['price_max'])
    if not items:
        context['error'] = "Sorry, no item matches your search\n"
    return context


def preprocess_query(query):
    error = ''
    try:
        price_min = int(query['price_min']) if int(query['price_min']) >= 0 else 0
    except ValueError or KeyError:
        price_min = 0
        error += 'Minimum price was not int or less than zero.\n'

    try:
        price_max = int(query['price_max']) if int(query['price_max']) > int(query['price_min']) else None
    except ValueError or KeyError:
        price_max = None
        error += 'Maximum price was not int or less than minimum price.\n'
        # categories = query['categories']
        # print("value or key error")
        # categories = []

    processed_query = {'query': str(query['query']).lower(),
                       'price_max': price_max,
                       'price_min': price_min,
                       # 'categories': categories
                       }

    return processed_query, error


def filter_price(results, price_min=0, price_max=None):
    if not price_min:
        price_min = 0

    if not price_max:
        results = results.filter(price__gte=price_min)
    else:
        results = results.filter(price__gte=price_min, price__lte=price_max)
    return results
