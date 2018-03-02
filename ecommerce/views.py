from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Item

def search(request):
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
    context = {'items' : None}
    items = Item.objects.all()
    if items:
        context['items'] = items

    return render(request, 'ecommerce/home.html', context)


def register_new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
    form = UserForm()
    return render(request, 'ecommerce/register.html', {'title': 'Register new user',
                                                       'form': form})

