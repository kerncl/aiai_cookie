from django.db import models
from account.models import Profile


# Create your models here.
class OrderModel(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start = models.DateField()
    end = models.DateField()
    total_price = models.DecimalField(max_digits=10,
                                      decimal_places=2)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{sum([item.quantity for item in self.orderitem_set.all()])} item with RM {self.total_price}"

    def __iter__(self):
        for item in self.orderitem_set.all():
            yield item


class OrderItem(models.Model):
    product = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    total_price = models.DecimalField(max_digits=10,
                                      decimal_places=2)
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} x {self.quantity}"
