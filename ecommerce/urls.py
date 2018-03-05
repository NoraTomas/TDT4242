from . import views
from django.contrib import admin
from django.urls import path, include
from .views import search, home
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name = "search" ),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^home/$', home, name = "home" ),
    url(r'^register/', views.register_new_user, name='register'),
    url(r'^cart/', views.view_cart, name='cart'),
    ##url(r'^$',views.home,name='home'),
    ##path('admin/',views.index1,name='index1'),
]
