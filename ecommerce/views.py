from ecommerce import settings
from django.shortcuts import render, get_object_or_404, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from django.template import loader
from django.contrib.auth.models import User



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


def register_new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
    form = UserForm()
    return render(request, 'ecommerce/register.html', {'title': 'Register new user',
                                                       'form': form})


def load_home_page(request):
    return render(request, 'ecommerce/home.html')

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'resultregistration/user_detail.html',
                  {'privatekey': user.pk})
