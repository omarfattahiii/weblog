from django.contrib import admin
from .models import SinglePost, SeriePostPart, SeriePost, UpdateRequest

admin.site.register(UpdateRequest)

class SeriePostPartInline(admin.TabularInline):
    model = SeriePostPart
    extra = 0

class SeriePostAdmin(admin.ModelAdmin):
    inlines = [SeriePostPartInline]
    list_display = ['title', 'slug', 'pub_date', 'up_date', 'author', 'is_published']
    list_filter = ['category', 'author', 'is_published', 'pub_date', 'up_date']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}

admin.site.register(SeriePost, SeriePostAdmin)

@admin.register(SinglePost)
class SinglePostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'pub_date', 'up_date', 'author', 'is_published']
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['title']
    list_filter = ['category', 'author', 'is_published', 'pub_date', 'up_date']
    fieldsets = [
        (
            "Base Data",
            {
                "fields": ['category', 'tag', 'title', 'description', 'slug'],
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
                "fields": ['is_published'],
            },
        ),
    ]
