from django.db import models

# Create your models here.
class StatisticCounter(models.Model):
    """
    date - дата события,
    views - количество показов,
    clicks - количество кликов,
    cost - стоимость кликов (в рублях с точностью до копеек)
    """
    date = models.DateField()
    views = models.IntegerField()
    clicks = models.IntegerField()
    cost = models.FloatField()