from django.shortcuts import render
from .models import Comments


def single_comments(requset, id):
    comments = Comments.objects.filter(single=id).order_by("-pub_date")
    context = {"comments": comments}
    template_name = "post/single_posts_detail.html"

    return render(requset, template_name, content)

def serie_comments(requset, id):
    comments = Comments.objects.filter(serie=id).order_by("-pub_date")
    context = {"comments": comments}
    template_name = "post/serie_posts_parts_detail.html"

    return render(requset, template_name, content)
