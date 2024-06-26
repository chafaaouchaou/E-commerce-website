"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ecomApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register.as_view(),name="register"),
    path("login/", logine.as_view(),name="login"),
    #google authentication should done in the forntend (remember)
    path('users/<int:pk>', userview.as_view(), name='user-list'),
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('wishlists/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('wishlist/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('wishlists/check/<int:product_id>/', ProductWishlistCheckView.as_view(), name='check-product-wishlist'),
    
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),

    path('cart-items/', CartProductCreateView.as_view(), name='cart-item-create'),
    path('cart-items/<int:pk>/', CartProductUpdateView.as_view(), name='cart-item-update'),
    path('cart-items/<int:pk>/delete/', CartProductDeleteView.as_view(), name='cart-item-delete'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    path('search/', search.as_view(), name='search-product'),
    path("stripe/",StripCheckoutView.as_view(),name="stripe"),
    path("success", success_callback, name="success"),
]

