from django.db import models

# Create your models here.

class TestTable(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)


class MenuItems(models.Model):


class Category(models.Model):


class Cuisine(models.Model):
