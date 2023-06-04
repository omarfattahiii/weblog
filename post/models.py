from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from tag.models import Tags
from tinymce import models as tinymce_models


class SinglePost(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    content = tinymce_models.HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    # TODO: comment field
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    lock = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tags)

    class Meta:
        verbose_name = "Single Post"
        verbose_name_plural = "Single Post's"

    def __str__(self):
        return self.title

class SeriePost(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    lock = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tags)

    class Meta:
        verbose_name = "Seire Post"
        verbose_name_plural = "Serie's Post's"

    def __str__(self):
        return self.title

class SeriePostPart(models.Model):
    seriepost = models.ForeignKey('SeriePost', on_delete=models.CASCADE)
    part = models.IntegerField(unique=True)
    title = title = models.CharField(max_length=255, unique=True)
    content = tinymce_models.HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    lock = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Seire Post Part"
        verbose_name_plural = "Serie Post Part's"

    def __str__(self):
        return f"{self.title} | {self.seriepost}"
