from django.db import models

# Create your models here.


class HistoricalData(models.Model):
    coin = models.ForeignKey(Coin)
    date = models.DateField()
    price = models.FloatField()
    market_cap = models.BigIntegerField()


class Coin(models.Model):
    name = models.CharField(max_length=200)
    short = models.CharField(max_length=200)