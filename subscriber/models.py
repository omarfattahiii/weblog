from django.db import models


class Subscriber(models.Model):
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscriber's"
