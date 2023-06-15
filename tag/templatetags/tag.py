from django import template
from tag.models import Tags

register = template.Library()

@register.inclusion_tag("tag/partials/all_tags.html")
def all_tags():
    try:
        tags = Tags.objects.all()

        return {'tags': tags}
    except Exception:
        print(Exception)
