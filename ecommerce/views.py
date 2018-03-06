from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Item, Category
from .search.search import process_query


def search(request):
    context = {'error': '',
               'categories': Category.objects.all(),
               'query': '',
               'price_min': None,
               'price_max': None}
    if request.method == 'GET' and request.GET:
        # results = Sear
        query = request.GET
        # print(query)
        if query:
            context = process_query(query)

    return render(request, "ecommerce/search.html", context=context)


def home(request):
    all_items = Item.objects.all()
    context = {'items': all_items}
    # items = Item.objects.all()
    # if items:
    #     context['items'] = items

    return render(request, 'ecommerce/home.html', context)


def register_new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
    form = UserForm()
    return render(request, 'ecommerce/register.html', {'title': 'Register new user',
                                                       'form': form})


def view_cart(request):
    current_user = request.user
    all_user_items = Item.objects.filter(owner=current_user)

    context = {
        'all_user_items': all_user_items
    }

    return render(request, 'ecommerce/view_cart.html', context)
