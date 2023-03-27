from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):

    food_name = models.CharField(max_length=100)
    carbs = models.FloatField(default='')
    protein = models.FloatField(default='')
    fats = models.FloatField(default='')
    calories = models.IntegerField(max_length=10, default='')


class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)


