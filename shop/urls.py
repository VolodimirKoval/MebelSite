from django.urls import path
from .views import products, current_product


app_name = 'shop'


urlpatterns = [
    path('products/', products, name='products'),
    path('current_product/', current_product, name='current_product'),
]
