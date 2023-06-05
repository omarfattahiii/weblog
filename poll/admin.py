from django.contrib import admin
from .models import Polls, PollsOption


class PollsOptionInline(admin.TabularInline):
    model = PollsOption

class PollsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'pub_date', 'up_date', 'author', 'lock']
    list_filter = ['category', 'author', 'lock', 'pub_date', 'up_date']
    inlines = [PollsOptionInline]
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Polls, PollsAdmin)
