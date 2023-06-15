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
    path('posts/', include('post.urls')),
    path('categories/', include('category.urls')),
    path('polls/', include('poll.urls')),
    path('advertisings/', include('advertising.urls')),
    path('presentations/', include('presentation.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('tinymce/', include('tinymce.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
