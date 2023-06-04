from django.shortcuts import render
from .models import Configuration


def layout(request):
    config = Configuration.objects.all()
    context = {'site': config}
    template_name = 'layout.html'

    return render(request, template_name, context)
