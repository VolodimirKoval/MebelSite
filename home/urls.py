from django.urls import path

from .views import main_page, about_us

app_name = 'main'

urlpatterns = [
    path('', main_page, name='main'),
    path('about/', about_us, name='about'),
]
