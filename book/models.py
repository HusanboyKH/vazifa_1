from django.db import models

from django.db import models
from datetime import datetime


# Create your models here.

class AuthorModel(models.Model):
    name = models.CharField(max_length=50, default='')
    fname = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField(default=datetime.now)
    class Meta:
        db_table = 'author'

class BookModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    page = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    class Meta:
        db_table = 'book'

