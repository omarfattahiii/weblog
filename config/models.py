from django.db import models
from ckeditor.fields import RichTextField
from post.models import SinglePost, SeriePost

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


class Reference(models.Model):
    single_post = models.ManyToManyField(SinglePost, blank=True)
    serie_post = models.ManyToManyField(SeriePost, blank=True)
    url = models.TextField()

    class Meta:
        verbose_name = "Post Reference"
        verbose_name_plural = "Post Reference's"

    def __str__(self):
        return f"{self.single_post}, {self.serie_post}"


class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact's"

    def __str__(self):
        return f"{self.name} - {self.subject[:50]}"


class News(models.Model):
    content = RichTextField()

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News's"

    def __str__(self):
        return self.content[:50]
