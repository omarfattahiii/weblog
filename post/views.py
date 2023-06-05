from django.shortcuts import render
from .models import SinglePost, SeriePost

def single_posts(request):
    objects = SinglePost.objects.all().order_by("up_date", "pub_date")
    context = {'objects': objects}
    template_name = 'post/single_posts.html'

    return render(request, template_name, context)

def serie_posts(request):
    objects = SeriePost.objects.all().order_by("up_date", "pub_date")
    context = {'objects': objects}
    template_name = 'post/serie_posts.html'

    return render(request, template_name, context)
