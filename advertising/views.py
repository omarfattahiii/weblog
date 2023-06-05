from django.shortcuts import render
from .models import Advertising


def advertising(request):
    objects = Advertising.objects.all()
    context = {'objects': objects}
    template_name = 'advertising/advertisings.html'

    return render(request, template_name, context)
