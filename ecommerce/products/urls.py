"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from products import views  
from django.conf import settings
from django.conf.urls.static import static
from .views import checkout, order_confirmation
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
def logout_redirect(request):
    return redirect('index')
def debug_urls(request):
    return HttpResponse("URL is working!")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='index'),
    path('products/', views.product_listing, name='products'),
    path('add_product/', views.add_product, name='add_product'),  
    path('test-url/', debug_urls),
    path('products/', views.product_listing, name='product_listing'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('products/', views.product_listing, name='product_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.landing_page, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', views.landing_page, name='index'),
    path('logout_redirect/', logout_redirect, name='logout_redirect'),
    path("register/", views.register, name="register"),
    path('popular-products/', views.popular_products, name='popular_products')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)