from django.db import models


class Posts(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=80)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title
