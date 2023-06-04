from django.contrib import admin
from .models import Polls, PollsOption


class PollsOptionInline(admin.TabularInline):
    model = PollsOption

class PollsAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'up_date', 'lock']
    inlines = [PollsOptionInline]


admin.site.register(Polls, PollsAdmin)
