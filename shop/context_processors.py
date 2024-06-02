from datetime import datetime
from shop.models import Category, Products


def site_name(request):
    return {'site_name': 'Mebel of your dream'}


def footer_name_date(request):
    current_date = datetime.now()
    return {'footer_name_date': f'Copyright © Mebel {current_date.year}'}


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def products(request):
    products = Products.objects.all()
    return {'products': products}
    