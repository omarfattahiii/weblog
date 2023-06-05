from django.contrib import admin
from .models import Presentation


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
        list_display = ['title', 'slug', 'pub_date', 'up_date', 'author', 'lock']
        list_filter = ['author', 'lock', 'pub_date', 'up_date']
        prepopulated_fields = {'slug': ['title']}
