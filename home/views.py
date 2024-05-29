from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import DataOnPage
import os


# def read_about_us():
#     file_path = os.path.join(os.path.dirname(__file__), 'about_us.txt')
#     with open(file_path, 'r', encoding='utf-8') as about_us_file:
#         return about_us_file.read()


def main_page(request: WSGIRequest) -> HttpResponse:
    context = {
        'title': 'Головна',
    }
    
    return render(request, 'home/main.html', context=context)


def about_us(request: WSGIRequest) -> HttpResponse:
    content = get_object_or_404(DataOnPage, page_name='about_us')
    context = {
        'title': content.title,
        'content': content,
    }
    return render(request, 'home/about_us.html', context=context)
