from django.db import models
from cofn.apps.authentication.models import User


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    body_text = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
