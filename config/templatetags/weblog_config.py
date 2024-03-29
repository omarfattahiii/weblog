from django import template
from config.models import Configuration, Notic

register = template.Library()


@register.inclusion_tag("config/partials/note.html")
def notic():
    notes = Notic.objects.all()
    context = {'notes': notes}

    return context


try:
    config = Configuration.objects.get(id=1)

    @register.simple_tag
    def site_title():
        title = config.site_title

        return title

    @register.simple_tag
    def site_header():
        header = config.site_header

        return header

    @register.simple_tag
    def meta_description():
        description = config.meta_description

        return description

    @register.simple_tag
    def meta_author():
        author = config.meta_author

        return author

    @register.simple_tag
    def meta_revised():
        revised = config.meta_revised

        return revised

    @register.simple_tag
    def about():
        site_about = config.site_about

        return site_about

    @register.simple_tag
    def icon():
        favicon = config.favicon

        return favicon

except:
    print("Configuration Obj Does not Exist.")
