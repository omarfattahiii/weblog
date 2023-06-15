from django.shortcuts import render, get_object_or_404
import random
from .models import SinglePost, SeriePost, SeriePostPart

def posts(request):
    single = SinglePost.objects.filter(is_published=True).order_by("-up_date", "-pub_date")
    serie = SeriePost.objects.filter(is_published=True).order_by("-up_date", "-pub_date")
    context = {'single': single, 'serie': serie}
    template_name = 'post/posts.html'

    return render(request, template_name, context)

def single_posts(request):
    objects = SinglePost.objects.filter(is_published=True).order_by("-up_date", "-pub_date")
    context = {'objects': objects}
    template_name = 'post/single_posts.html'

    return render(request, template_name, context)

def single_posts_detail(request, id):
    object = get_object_or_404(SinglePost, pk=id, is_published=True)
    context = {'object': object}
    template_name = 'post/single_posts_detail.html'

    return render(request, template_name, context)


def serie_posts(request):
    objects = SeriePost.objects.filter(is_published=True).order_by("-up_date", "-pub_date")
    context = {'objects': objects}
    template_name = 'post/serie_posts.html'

    return render(request, template_name, context)

def serie_posts_detail(request, id):
    object = get_object_or_404(SeriePost, pk=id, is_published=True)
    object_parts = SeriePostPart.objects.filter(seriepost=object, is_published=True)
    context = {'object': object, 'object_parts': object_parts}
    template_name = 'post/serie_posts_detail.html'

    return render(request, template_name, context)


def serie_posts_parts_detail(request, id, part_id):
    object = SeriePostPart.objects.get(id=part_id)
    context = {'object': object}
    template_name = 'post/serie_posts_parts_detail.html'

    return render(request, template_name, context)
