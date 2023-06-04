from django.db import models


class ParentCategory(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Category(models.Model):
    parent = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
