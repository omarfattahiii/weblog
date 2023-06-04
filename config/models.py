from django.db import models


class Configuration(models.Model):
    site_title = models.TextField()
    site_header = models.TextField()
    site_index_title = models.TextField()
    site_description = models.TextField()
    site_tags = models.TextField()
    site_about = models.TextField()
    site_contact = models.TextField()
    site_social_media = models.TextField()
    site_footer = models.TextField()

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration's"

    def __srt__(self):
        return "Site Configuration"
