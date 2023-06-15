from django.db import models
from ckeditor.fields import RichTextField

class Configuration(models.Model):
    site_title = models.TextField()
    site_header = models.TextField()
    site_about = models.TextField()
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    meta_author = models.TextField()
    meta_revised = models.DateTimeField(auto_now=True)
    favicon = models.ImageField(upload_to="weblog/configuration/favicon", blank=False, null=False)

    class Meta:
        verbose_name = "WebLog Configuration"
        verbose_name_plural = "WebLog Configuration's"

    def __str__(self):
        return self.site_title


class Notic(models.Model):
    content = RichTextField()

    class Meta:
        verbose_name = "WebLog Notic"
        verbose_name_plural = "WebLog Notic's"

    def __str__(self):
        return self.content[:30]
