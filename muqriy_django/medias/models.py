from django import forms
from django.db import models



# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.username}"


class Media(models.Model):
    id = models.AutoField(primary_key=True)
    category_one = models.CharField(verbose_name="Category_one", max_length=100, null=True)
    subcategory_one = models.CharField(verbose_name="Subcategory_one", max_length=100, default=False)
    category_two = models.CharField(verbose_name="Category_two", max_length=100, blank=True, null=True)
    subcategory_two = models.CharField(verbose_name="Subcategory_two", max_length=100, blank=True, null=True)
    type = models.CharField(verbose_name="Type", default=False, blank=True)
    media_group = models.BooleanField(verbose_name="Media group", default=False)
    file_id = models.CharField(verbose_name="File ID", max_length=100, blank=True, null=True)
    caption = models.TextField(verbose_name="Caption", max_length=4000, blank=True, null=True)
    description = models.TextField(verbose_name="Description", max_length=4000, blank=True, null=True)
    callback = models.CharField(verbose_name="Callback", max_length=60, blank=True, null=True)

    def __str__(self):
        return f"№{self.id} - {self.category_one}"
