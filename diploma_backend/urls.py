"""diploma_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from authorization.views import LoginView, SignupView, SignOutView
from basket.views import BasketView
from catalog.views import product_catalog_view, get_categories
from django.contrib import admin
from django.urls import path, include
from product.views import get_popular_products, get_limited_products, get_product
from sales.views import get_sales
from tags.views import get_tags
from order.views import OrderPlacing, OrderHistory, OrderDetail, OrderRetryPayment
from user_profiles.views import ProfileView, PostProfilePasswordView, PostProfileAvatarView
from payment.views import payment_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("frontend.urls")),
    path('api/sign-in/', LoginView.as_view(), name='api_login'),
    path('api/sign-up/', SignupView.as_view(), name='api_sign_up'),
    path('api/sign-out', SignOutView.as_view(), name='api_sign_out'),
    path('api/catalog/', product_catalog_view, name='api_catalog'),
    path('api/tags', get_tags, name='frontend:get_tags'),
    path('api/categories', get_categories, name='api_categories'),
    path('api/banners', get_popular_products, name='api_popular_products'),
    path('api/products/popular', get_popular_products, name='api_popular_products'),
    path('api/products/limited', get_limited_products, name='get_limited_products'),
    path('api/product/<int:pk>', get_product, name='api_product'),
    path('api/basket/', BasketView.as_view(), name='get_basket'),
    path('api/basket', BasketView.as_view(), name='post_basket'),
    path('api/basket/<int:pk>/', BasketView.as_view(), name='delete_basket'),
    path('api/sales', get_sales, name='get_sales'),
    path('api/orders', OrderPlacing.as_view(), name='orders'),
    path('api/order/<int:pk>', OrderPlacing.as_view(), name='order_detail'),
    path('api/history-order/', OrderHistory.as_view(), name='order-history'),
    path('api/order-detail/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('api/order-retry-payment/<int:pk>/', OrderRetryPayment.as_view(), name='order-retry-payment'),
    path('api/profile', ProfileView.as_view(), name='get_profile'),
    path('api/profile/password', PostProfilePasswordView.as_view(), name='post_profile_password'),
    path('api/profile/avatar', PostProfileAvatarView.as_view(), name='post_profile_avatar'),
    path('api/payment/<int:pk>', payment_view, name='payment_view'),
]
