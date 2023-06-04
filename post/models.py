from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from tinymce import models as tinymce_models


class SinglePost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    content = tinymce_models.HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    # TODO: comment field
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    lock = models.BooleanField(default=False)

    def __str__(self):
        return self.title
