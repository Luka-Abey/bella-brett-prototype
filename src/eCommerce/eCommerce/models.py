from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    pass


class OrderItem(models.Model):
    pass


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(auto_now_add=False)