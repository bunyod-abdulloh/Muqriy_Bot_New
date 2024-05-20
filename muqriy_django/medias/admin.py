from django.contrib import admin

# Register your models here.

from .models import User, Media

admin.site.register(User)
admin.site.register(Media)
