from django.shortcuts import render
from decouple import config
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact, Reference
from post.models import SinglePost, SeriePost


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

        RAYGANSMS = "https://RayganSMS.com/SendMessageWithPost.ashx"

        USERNAME = config('USERNAME')
        PASSWORD = config('PASSWORD')
        PHONENUMBER = config('PHONENUMBER')
        MESSAGE = f"یک پیام جدید از {name} با ایمیل {email}."
        RECNUMBER = config('RECNUMBER')
        SMSCLASS = 1

        messages.success(request, "پیام شما هم اکنون ارسال شد.")
        return HttpResponseRedirect(reverse('config:contact'))

    template_name = 'config/contact.html'
    return render(request, template_name, {})


def reference(request):
    reference = Reference.objects.all()
    context = {'reference': reference}

    template_name = 'config/reference.html'
    return render(request, template_name, context)

def search(request):
    if request.method == 'GET':
        query = request.GET['q']
        single_post = SinglePost.objects.filter(title__contains=query)
        serie_post = SeriePost.objects.filter(title__contains=query)

    context = {'single': single_post, 'serie': serie_post, 'query': query}

    template_name = 'config/search.html'
    return render(request, template_name, context)
