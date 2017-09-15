from rest_framework import serializers
from api.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'created', 'name', 'describe', 'price', 'isDelete')