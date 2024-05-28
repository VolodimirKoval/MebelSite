from django.contrib.auth.models import AbstractUser
from django.db import models
import os
from datetime import datetime


def auto_fill_user_image(instance, filename):
    current_data = datetime.now()
    return os.path.join(f"users_images/{current_data.year}/{instance.username}/{filename}")


class User(AbstractUser):
    image = models.ImageField(upload_to=auto_fill_user_image, null=True, blank=True, verbose_name="Зображення користувача")
    
    class Meta:
        db_table = "Користувачі"
        verbose_name = "користувач"
        verbose_name_plural = "Користувачі"
    
    def __str__(self):
        return self.username
    