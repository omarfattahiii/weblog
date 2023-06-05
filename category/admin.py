from django.contrib import admin
from .models import ParentCategory, Category

class CategoryInline(admin.TabularInline):
    model = Category
    prepopulated_fields = {'slug': ['title']}

class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    inlines = [CategoryInline]
    prepopulated_fields = {'slug': ['title']}

admin.site.register(ParentCategory, ParentCategoryAdmin)
