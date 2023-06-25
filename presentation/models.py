from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Presentation(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    content = RichTextField()
    is_published = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Presentation"
        verbose_name_plural = "Presentation's"

    def __str__(self):
        return self.title
