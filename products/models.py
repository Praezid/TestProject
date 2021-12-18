from django.db import models
from django.urls import reverse


class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        res = f"ID: {str(self.id)} Name: {str(self.name)} Price: {str(self.price)}"
        return res
