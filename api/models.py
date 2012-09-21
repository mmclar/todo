from django.db import models

class List(models.Model):
    title = models.CharField(max_length=200)

class Item(models.Model):
    list = models.ForeignKey(List)
    text = models.CharField(max_length=200)

