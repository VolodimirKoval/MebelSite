from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def products(request: WSGIRequest) -> HttpResponse:
    context = {
        'title': 'Продукти',
    }
    return render(request, 'shop/products.html', context=context)


def current_product(request: WSGIRequest) -> HttpResponse:
    context = {
        'title': 'Інфо по продукту',
    }
    return render(request, 'shop/current_product.html', context=context)
