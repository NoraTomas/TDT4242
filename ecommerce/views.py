from ecommerce import settings
from django.shortcuts import render, get_object_or_404, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.template import loader
from .models import Item


def search(request):
    """Process query from request, return the queryset as context with template."""
    context = {'message': ''}
    if request.method == 'GET' and request.GET:
        # results = Sear
        result = request.GET
        print(request.GET)
        query = result['query']
        print(query)
        if query:
            context['message'] = query
    return render(request, "ecommerce/search.html", context=context)


def home(request):
    """Render homepage showing searchbar and list of items."""
    context = {'items': None}
    items = Item.objects.all()
    if items:
        context['items'] = items

    return render(request, 'ecommerce/home.html', context)


def register_new_user(request):
    """Render page for registering a new user and render input from same page"""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
    form = UserForm()
    return render(request, 'ecommerce/register.html', {'title': 'Register new user',
                                                       'form': form})
