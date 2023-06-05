from django.shortcuts import render
from .models import ParentCategory


def parent_category(request):
    objects = ParentCategory.objects.all()
    context = {'objects': objects}
    template_name = 'category/parent_categories.html'

    return render(request, template_name, context)
