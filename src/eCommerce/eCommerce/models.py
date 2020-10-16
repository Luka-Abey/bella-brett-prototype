from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    pass


class OrderItem(models.Model):
    pass


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(auto_now_add=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username