from django.shortcuts import render
from .models import Polls, PollsOption


def polls(request):
    objects = Polls.objects.all()
    poll_option = PollsOption.objects.all()
    context = {'objects': objects, 'poll_option': poll_option}
    template_name = 'poll/polls.html'

    return render(request, template_name, context)
