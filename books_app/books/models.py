from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
