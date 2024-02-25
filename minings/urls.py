from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from minings_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("minings_app.urls")),


    path('', views.GetServices, name='services'),
    path('service/<int:id>/', views.GetService, name='service'),
    path('delete_service/<int:id>/', views.delete_service, name='delete_service'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),

]
