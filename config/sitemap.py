from django.contrib.sitemaps import Sitemap
from post.models import SinglePost, SeriePost


class SinglePostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return SinglePost.objects.filter(lock=False)

    def lastmod(self, obj):
        return obj.up_date


class SeriePostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return SeriePost.objects.filter(lock=False)

    def lastmod(self, obj):
        return obj.up_date
