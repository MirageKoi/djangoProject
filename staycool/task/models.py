from django.db import models


class Article(models.Model):
    name = models.CharField( max_length=50)
    title = models.CharField( max_length=50)


class Hello(models.Model):
    name = models.CharField( max_length=50)