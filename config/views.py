from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Contact


def index(request):
    context = {}
    template_name = 'index.html'
    return render(request, template_name, context)

def about(request):
    context = {}
    template_name = 'config/about.html'
    return render(request, template_name, context)

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        new_contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        new_contact.save()

        return HttpResponseRedirect(reverse('config:contact'))

    template_name = 'config/contact.html'
    return render(request, template_name, {})
