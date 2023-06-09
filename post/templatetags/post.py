from django import template
from post.models import SinglePost, SeriePost

register = template.Library()

@register.inclusion_tag("post/partials/last_single_post.html")
def last_single_post():
    try:
        single = SinglePost.objects.filter(is_published=True).order_by("-up_date", "-pub_date")[:5]

        return {'single': single}
    except Exception:
        print(Exception)

@register.inclusion_tag("post/partials/last_serie_post.html")
def last_serie_post():
    try:
        serie = SeriePost.objects.filter(is_published=True).order_by("-up_date", "-pub_date")[:5]

        return {'serie': serie}
    except Exception:
        print(Exception)
