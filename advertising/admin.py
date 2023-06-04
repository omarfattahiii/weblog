from django.contrib import admin
from .models import Advertising


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
        list_disply = ['title', 'category', 'slug', 'lock']
        search_list = ['title', 'content']
