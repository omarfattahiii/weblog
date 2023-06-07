from django.db import models

class Configuration(models.Model):
    site_title = models.TextField()
    site_header = models.TextField()
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    meta_author = models.TextField()
    meta_revised = models.DateTimeField(auto_now=True)
    favicon = models.ImageField(upload_to="weblog/configuration/favicon")

    class Meta:
        verbose_name = "WebLog Configuration"
        verbose_name_plural = "WebLog Configuration's"

    def __str__(self):
        return self.site_title
