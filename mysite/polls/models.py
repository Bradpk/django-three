from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)

class Pizza(models.Model):
    size = models.IntegerField()
    toppings = models.ManyToManyField(Topping)