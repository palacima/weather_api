from django.db import models

class Weather(models.Model):
    lat = models.FloatField(max_length=25)
    long = models.FloatField(max_length=25)
    temp = models.CharField(max_length=100)

    def _str_(self): #show the actual city name on the dashboard
        return self.name
