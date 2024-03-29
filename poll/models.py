from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Polls(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.TextField()
    slug = slug = models.SlugField(max_length=50, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Poll's"

    def __str__(self):
        return self.title


class PollsOption(models.Model):
    poll = models.ForeignKey(
        'Polls', on_delete=models.CASCADE, related_name="poll_option")
    title = models.CharField(max_length=30, unique=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Poll Option"
        verbose_name_plural = "Poll Option's"

    def __str__(self):
        return self.title


class Vote(models.Model):
    poll = models.ForeignKey(
        'Polls', on_delete=models.CASCADE, related_name="poll_vote")
    option = models.ForeignKey(
        'PollsOption', on_delete=models.CASCADE, related_name="poll_vote")

    class Meta:
        verbose_name = "Poll Vote"
        verbose_name_plural = "Poll Vote's"

    def __str__(self):
        return f"{self.poll}-{self.option}"
