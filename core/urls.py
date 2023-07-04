from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from config.sitemap import SinglePostSitemap, SeriePostSitemap

sitemaps = {
    'single_posts': SinglePostSitemap,
    'serie_posts': SeriePostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('config.urls')),

    path('psts/', include('post.urls')),
    path('ctgrs/', include('category.urls')),
    path('plls/', include('poll.urls')),
    path('prsntns/', include('presentation.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
