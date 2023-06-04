from django.shortcuts import render
from .models import SinglePost

def posts(request):
    objects = SinglePost.objects.all().order_by("up_date", "pub_date")
    context = {'objects': objects}
    template_name = 'post/posts.html'

    return render(request, template_name, context)
