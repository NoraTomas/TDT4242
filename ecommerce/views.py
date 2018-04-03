from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Item, Category
from .search.search import process_query
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from .forms import HomeForm
from django.shortcuts import render


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
    items_in_cart = 0

    current_user = request.user
    current_user_owned_items = Item.objects.filter(owner=current_user)

    for current_user_owned_item in current_user_owned_items:
        items_in_cart += 1

    for item in all_items:
        if item.sale > 0:
            sale_percent = float(item.sale) / float(100)
            new_price_percent = 1 - sale_percent
            item_price_with_sale = float(item.price) * new_price_percent

            item.price = item_price_with_sale

    context = {'items': all_items, 'items_in_cart': items_in_cart}

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




@login_required
class HomeView(TemplateView):
    def add_item(request, pk):
        item = Item.objects.get(pk=pk)
        current_user = request.user
        owner = item.owner
        owner.add(current_user)
        all_user_items = Item.objects.filter(owner=current_user)

        context = {
            'all_user_items': all_user_items
        }
        return render(request, 'ecommerce/view_cart.html', context)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'ecommerce/signup.html'

