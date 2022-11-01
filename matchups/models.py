from django.db import models
from django.conf import settings


class Character(models.Model):
    name = models.CharField(max_length=30)
    picture = models.URLField()
    description = models.TextField()
    number = models.IntegerField()
