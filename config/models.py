from django.db import models
from ckeditor.fields import RichTextField
from post.models import SinglePost, SeriePost


class Configuration(models.Model):
    site_title = models.TextField(blank=True, null=True)
    site_header = models.TextField(blank=True, null=True)
    site_about = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_author = models.TextField(blank=True, null=True)
    meta_revised = models.DateTimeField(auto_now=True, blank=True, null=True)
    favicon = models.ImageField(
        upload_to="weblog/configuration/favicon", blank=True, null=True)

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
    single_post = models.ForeignKey(SinglePost, on_delete=models.CASCADE, blank=True, null=True)
    serie_post = models.ForeignKey(SeriePost, on_delete=models.CASCADE, blank=True, null=True)
    url = models.URLField(max_length=255)

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


class Subscriber(models.Model):
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscriber's"
