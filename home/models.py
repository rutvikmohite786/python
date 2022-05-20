from django.db import models
class PriceHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.PositiveIntegerField(),
# Create your models here.
class Pricetable(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.PositiveIntegerField(),

class UserData(models.Model):
    name = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254),

def __str__(self):
        return self.name
    