from django.db import models
from django.contrib.auth.models import User
from post.models import SinglePost, SeriePost


class Comments(models.Model):
    single = models.ForeignKey(SinglePost, on_delete=models.CASCADE, related_name='single_comments', blank=True, null=True)
    serie = models.ForeignKey(SeriePost, on_delete=models.CASCADE, related_name='serie_comments', blank=True, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}-{self.content[:30]}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comment's"
