from django.contrib import admin
from .models import ParentCategory, Category

class CategoryInline(admin.TabularInline):
    model = Category

class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    inlines = [CategoryInline]

admin.site.register(ParentCategory, ParentCategoryAdmin)
