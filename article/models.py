from django.db import models

# Create your models here.
class Article():
    author = models.ForeignKey()
    title = models.CharField()
    content = models.TextField()
