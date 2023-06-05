from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('config.urls')),
    path('posts/', include('post.urls')),
    path('categories/', include('category.urls')),
    path('polls/', include('poll.urls')),
    path('advertisings/', include('advertising.urls')),
    path('presentations/', include('presentation.urls')),

    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
