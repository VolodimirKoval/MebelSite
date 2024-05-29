from django.db import models


class DataOnPage(models.Model):
    page_name = models.CharField(max_length=100, verbose_name="Назва сторінки")
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="Заголовок")
    text = models.TextField(null=True, blank=True, editable=True, verbose_name="Текст")
    
    class Meta:
        db_table = "Текстові дані на сторінці"
        verbose_name = "текстові дані на сторінці"
        verbose_name_plural = "Текстові дані на сторінці"
    
    def __str__(self):
        return self.page_name
    