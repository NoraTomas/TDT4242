from ..models import *
from simple_search import search_filter


def search_store(query):
    error = ''
    search_fields = ['^name', 'author__last_name', 'author__first_name']
    results = Item.objects.filter(search_filter(search_fields, query['query']))

    if not query['query'] and (query['authors'] or query['categories']):
        results = Item.objects.all()

    results = filter_author(results, query['authors'])
    results = filter_categories(results, query['categories'])
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
        context['error'] += "Sorry, no item matches your search\n"
    return context


def preprocess_query(query):
    error = ''
    try:
        price_min = query['price_min']
        price_min = int(price_min) if int(price_min) >= 0 else 0
    except Exception:   # Could not find MultiValueDictError
        price_min = 0
        error += ''# 'Minimum price was not int or less than zero.\n'

    try:
        price_max = int(query['price_max']) if int(query['price_max']) > int(query['price_min']) else None
    except Exception:  # Could not find MultiValueDictError
        price_max = None
        error += '' #''Maximum price was not int or less than minimum price.\n'
        # categories = query['categories']
        # print("value or key error")
        # categories = []

    try:
        categories = query['categories'].split(';')
        print("categories:", categories)
    except Exception:
        categories = []
        error += '\n No categories specified'

    try:
        authors = query['authors'].split(';')
        print("authors:", authors)
    except Exception:
        authors = []
        error += '\n No authors specified'

    processed_query = {'query': str(query['query']).lower(),
                       'price_max': price_max,
                       'price_min': price_min,
                       'categories': categories,
                       'authors': authors
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


def filter_author(results, authors=()):
    if not authors:
        return results
    else:
        search_fields = ['^last_name', 'first_name']
        authors_string = ''
        for a in authors:
            authors_string += str(a)
        author_ids = Author.objects.filter((search_filter(search_fields, authors_string)))
        return results.filter(author__in=author_ids)


def filter_categories(results, categories=()):
    if not categories:
        return results
    else:
        categories_string = ''
        for c in categories:
            categories_string += str(c)
        search_fields = ['^name']
        category_ids = Category.objects.filter(search_filter(search_fields, categories_string))
        return results.filter(category__in=category_ids)
