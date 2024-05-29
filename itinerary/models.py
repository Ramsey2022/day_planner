from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Park(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    rating = models.IntegerField()

    class Meta:
        managed = False

    def __str__(self):
        return self.name


class Weather(models.Model):
    day = models.CharField(max_length=255)
    date = models.DateField()
    temp = models.IntegerField()
    main = models.CharField(max_length=255)

    class Meta:
        managed = False

    def __str__(self):
        return self.date
