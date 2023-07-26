from django.db import models

# Create your models here.

class TestTable(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)


class MenuItems(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.CharField(max_length=200, null=False, blank=False, unique=True)
    price = models.CharField(max_length=200, null=False, blank=False, unique=True)
    #fktocategory = models.CharField(max_length=200, null=False, blank=False, unique=True)  <--- WTF is FK to Category
    #fktocuisine = models.CharField(max_length=200, null=False, blank=False, unique=True)   <--- WTF is FK to Cuisine
     


class Category(models.Model):
    appetizer = models.CharField(max_length=200, null=False, blank=False, unique=True)
    dessert = models.CharField(max_length=200, null=False, blank=False, unique=True)
    maindish = models.CharField(max_length=200, null=False, blank=False, unique=True)
# What is this and what else is needed


class Cuisine(models.Model):
        american = models.CharField(max_length=200, null=False, blank=False, unique=True)
        thai = models.CharField(max_length=200, null=False, blank=False, unique=True)
# What is this and what else is needed


