from django.shortcuts import render
from .models import Presentation


def presentation(request):
    objects = Presentation.objects.all()
    context = {'objects': objects}
    template_name = 'presentation/presentations.html'

    return render(request, template_name, context)

def presentation_detail(request, id):
    object = Presentation.objects.get(pk=id)
    context = {'object': object}
    template_name = 'presentation/presentation_detail.html'

    return render(request, template_name, context)
