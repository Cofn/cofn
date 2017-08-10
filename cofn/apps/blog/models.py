from django.db import models


class Posts(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=80)
    bodytext = models.TextField()
    timestamp = models.TimeField()