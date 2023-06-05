from django.shortcuts import render


def index(request):
    context = {}
    template_name = 'index.html'
    return render(request, template_name, context)

def about(request):
    context = {}
    template_name = 'config/about.html'
    return render(request, template_name, context)

def contact(request):
    context = {}
    template_name = 'config/contact.html'
    return render(request, template_name, context)
