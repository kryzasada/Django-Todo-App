from django.contrib import admin

# Register your models here.

from .models import UserPosts

admin.site.register(UserPosts)