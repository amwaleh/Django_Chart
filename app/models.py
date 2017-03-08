from django.db import models

# Create your models here.
class Population(models.Model):
    country = models.TextField(max_length=64, unique=True)
    Population = models.IntegerField

    def __str__(self):
        return self.country

