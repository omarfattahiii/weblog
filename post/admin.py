from django.contrib import admin
from .models import SinglePost, SeriePostPart, SeriePost


class SeriePostPartInline(admin.TabularInline):
    model = SeriePostPart

class SeriePostAdmin(admin.ModelAdmin):
    inlines = [SeriePostPartInline]

admin.site.register(SeriePost, SeriePostAdmin)

@admin.register(SinglePost)
class SinglePostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'pub_date', 'up_date', 'author', 'lock']
    # TODO: search items
    list_filter = ['category', 'author', 'lock', 'pub_date', 'up_date']
    fieldsets = [
        (
            "Base Data",
            {
                "fields": ['category', 'title'],
            },
        ),

        (
            "Content",
            {
                "fields": ['content'],
            },
        ),

        (
            "Status",
            {
                "classes": ["collapse"],
                "fields": ['lock'],
            },
        ),
    ]
