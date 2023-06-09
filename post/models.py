from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from django.urls import reverse
from django.contrib.auth.models import User
from category.models import Category
from tag.models import Tags
from ckeditor.fields import RichTextField


class SinglePost(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tags)
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name = "Single Post"
        verbose_name_plural = "Single Post's"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:single_posts_detail", kwargs={'slug': self.slug})

class SeriePost(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tags)

    class Meta:
        verbose_name = "Seire Post"
        verbose_name_plural = "Serie's Post's"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:serie_posts_detail", kwargs={'slug': self.slug})


class SeriePostPart(models.Model):
    seriepost = models.ForeignKey('SeriePost', on_delete=models.CASCADE)
    part = models.IntegerField()
    title = title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name = "Seire Post Part"
        verbose_name_plural = "Serie Post Part's"

    def __str__(self):
        return f"{self.title} | {self.seriepost}"
