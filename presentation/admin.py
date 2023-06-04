from django.contrib import admin
from .models import Presentation


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
        list_disply = ['title', 'slug', 'lock']
        search_list = ['title', 'content']
