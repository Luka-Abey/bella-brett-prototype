from django.db import models
from django.contrib.auth.models import User

# SIZE_CHOICES = (
#     ('S', 'Small'),
#     ('M', 'Medium'),
#     ('L', 'Large')
# )

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.CharField(max_length=255)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    delivery_address = models.CharField(max_length=255)
    ordered = models.BooleanField(default=False)
    date = models.DateTimeField()

    def __str__(self):
        return self.name