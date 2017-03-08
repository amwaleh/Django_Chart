from django.db import models


class Population(models.Model):
    country = models.CharField(max_length=64)
    population = models.IntegerField()


class Ping(models.Model):
    CHOICES =[('UP','UP'),('DOWN','DOWN')]
    date = models.DateField()
    Ping = models.TextField(max_length=25, choices=CHOICES)
    name = models.TextField(max_length=64)

