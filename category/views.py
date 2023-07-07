from django.shortcuts import render
from .models import ParentCategory, Category


def parent_category(request):
    parent = ParentCategory.objects.all()
    child = Category.objects.all()
    context = {'parent': parent, 'child': child}
    template_name = 'category/parent_categories.html'

    return render(request, template_name, context)


def child_category(request, id):
    child = Category.objects.get(pk=id)
    context = {'child': child}
    template_name = 'category/child_categories.html'

    return render(request, template_name, context)
