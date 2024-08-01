from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    cnm = models.CharField(max_length=50)
    product = models.CharField(max_length=40)
    quantity = models.IntegerField()
    price = models.IntegerField()
    delivery_date=models.DateField()