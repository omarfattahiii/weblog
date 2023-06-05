from django.shortcuts import render, get_object_or_404
from .models import SinglePost, SeriePost

def posts(request):
    single = SinglePost.objects.all().order_by("up_date", "pub_date")
    serie = SeriePost.objects.all().order_by("up_date", "pub_date")
    context = {'single': single, 'serie': serie}
    template_name = 'post/posts.html'

    return render(request, template_name, context)

def single_posts(request):
    objects = SinglePost.objects.all().order_by("up_date", "pub_date")
    context = {'objects': objects}
    template_name = 'post/single_posts.html'

    return render(request, template_name, context)

def single_posts_detail(request, pk):
    object = get_object_or_404(SinglePost, id=pk)
    context = {'object': object}
    template_name = 'post/single_posts_detail.html'

    return render(request, template_name, context)

def serie_posts(request):
    objects = SeriePost.objects.all().order_by("up_date", "pub_date")
    context = {'objects': objects}
    template_name = 'post/serie_posts.html'

    return render(request, template_name, context)

def serie_posts_detail(request, pk):
    object = get_object_or_404(SeriePost, id=pk)
    context = {'object': object}
    template_name = 'post/serie_posts_detail.html'

    return render(request, template_name, context)
