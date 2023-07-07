from django.contrib import admin
from .models import Polls, PollsOption, Vote


admin.site.register(Vote)


class PollsOptionInline(admin.TabularInline):
    model = PollsOption
    extra = 4


class PollsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'pub_date',
                    'up_date', 'author', 'is_published']
    list_filter = ['category', 'author', 'is_published', 'pub_date', 'up_date']
    inlines = [PollsOptionInline]
    prepopulated_fields = {'slug': ['title']}


admin.site.register(Polls, PollsAdmin)
