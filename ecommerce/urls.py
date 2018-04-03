from . import views
from django.contrib import admin
from django.urls import path, include
from .views import search, home
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name = "search" ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    url(r'^home/$', home, name = "home" ),
    url(r'^cart/', views.view_cart, name='cart'),
    url(r'^add_item/(?P<pk>\d+)/$', views.HomeView.add_item, name='add_item'),

]
