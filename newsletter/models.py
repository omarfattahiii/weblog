from django.db import models


class Email(models.Model):
    email = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Email's"

    def __str__(self):
        return self.email
