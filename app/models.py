from django.db import models



class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country)
    population = models.IntegerField()
    city = models.CharField(max_length=64, default=None)

    def __str__(self):
        return '{} : {}'.format(self.city, self.population)
