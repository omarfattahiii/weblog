from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Subscriber


def submit(request):
    if request.method == 'POST':
        email = request.POST['email']
        new_email = Subscriber.objects.create(email=email)
        new_email.save()

        messages.success(request, 'منتظر ایمیل از طرف ما باشید!')
    return HttpResponseRedirect(reverse('config:index'))
