from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    price = serializers.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'price')
