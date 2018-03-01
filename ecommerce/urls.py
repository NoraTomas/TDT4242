from . import views
from django.contrib import admin
from django.urls import path
from .views import search
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name = "search" ),
    url(r'^register/', views.register_new_user, name='register'),
    url(r'^home/', views.load_home_page, name='home'),
    url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail')

]
