from . import views
from django.contrib import admin
from django.urls import path, include
from .views import search, home
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name = "search" ),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^home/$', home, name = "home" ),
    url(r'^register/', views.register_new_user, name='register'),
    url(r'^cart/', views.view_cart, name='cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

