from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from post.models import SinglePost, SeriePost


class SinglePostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return SinglePost.objects.filter(is_published=True).order_by('-pub_date')

    def lastmod(self, obj):
        return obj.up_date

    def location(self, obj):
        return reverse('post:single_posts_detail', kwargs={'id': obj.id})


class SeriePostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return SeriePost.objects.filter(is_published=True).order_by('-pub_date')

    def lastmod(self, obj):
        return obj.up_date

    def location(self, obj):
        return reverse('post:serie_posts_detail', kwargs={'id': obj.id})
