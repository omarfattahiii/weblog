from django.shortcuts import render
from .models import Polls


def polls(request):
    objects = Polls.objects.all()
    context = {'objects': objects}
    template_name = 'poll/polls.html'

    return render(request, template_name, context)
