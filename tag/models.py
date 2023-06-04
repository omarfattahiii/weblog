class Tags(models.Model):
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tag's"

    def __str__(self):
        return self.title
