from django.contrib import admin
from .models import DataOnPage


@admin.register(DataOnPage)
class DataOnPageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'text')
