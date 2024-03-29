from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from category.models import Category
from tag.models import Tags
from ckeditor.fields import RichTextField


class SinglePost(models.Model):
    category = models.ManyToManyField(Category, related_name="single_post")
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tags, related_name="single_post_tag")
    comment = models.ManyToManyField("Comments", related_name="single_post")

    class Meta:
        verbose_name = "Single Post"
        verbose_name_plural = "Single Post's"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:single_posts_detail", kwargs={'slug': self.slug})

class SeriePost(models.Model):
    category = models.ManyToManyField(Category, related_name="serie_post")
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tags, related_name="serie_post_tag")

    class Meta:
        verbose_name = "Seire Post"
        verbose_name_plural = "Serie's Post's"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post:serie_posts_detail", kwargs={'slug': self.slug})


class SeriePostPart(models.Model):
    seriepost = models.ForeignKey('SeriePost', on_delete=models.CASCADE, related_name="serie_post")
    part = models.IntegerField()
    title = title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    comment = models.ManyToManyField("Comments", related_name="serie_post")

    class Meta:
        verbose_name = "Seire Post Part"
        verbose_name_plural = "Serie Post Part's"

    def __str__(self):
        return f"{self.title} | {self.seriepost}"


class Comments(models.Model):
    single = models.ForeignKey("SinglePost", on_delete=models.CASCADE, null=True, blank=True)
    serie = models.ForeignKey("SeriePostPart", on_delete=models.CASCADE, null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}-{self.content[:30]}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comment's"


class UpdateRequest(models.Model):
    post_title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Post Update Request"
        verbose_name_plural = "Post Update Request's"

    def __str__(self):
        return self.post_title
