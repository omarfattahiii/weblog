from django import template
import random
from collections import OrderedDict
from post.models import SinglePost, SeriePost

register = template.Library()

@register.inclusion_tag("post/partials/random_single_posts.html")
def random_single_posts():
    single = SinglePost.objects.filter(is_published=True).order_by("-up_date", "-pub_date")
    single_posts_randomly = random.choices(single, k=3)

    return {'single_posts_randomly': single_posts_randomly}

@register.inclusion_tag("post/partials/random_serie_posts.html")
def random_serie_posts():
    serie = SeriePost.objects.filter(is_published=True).order_by("-up_date", "-pub_date")
    serie_posts_randomly = random.choices(serie, k=3)

    return {'serie_posts_randomly': serie_posts_randomly}
