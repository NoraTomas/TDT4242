from . import views
from django.contrib import admin
from django.urls import path
from .views import search
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name = "search" ),
    url(r'^register/', views.UserFormView.as_view(), name='register')

]
