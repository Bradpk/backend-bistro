from django.db import models

# Create your models here.

class TestTable(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
#-------------------------------------------------------------------------------------------------------------------------------
class TestTableTwo(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
#-------------------------------------------------------------------------------------------------------------------------------
class TestTableThree(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
#-------------------------------------------------------------------------------------------------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#-------------------------------------------------------------------------------------------------------------------------------
class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
#-------------------------------------------------------------------------------------------------------------------------------
class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    spicy_level = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    






