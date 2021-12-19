from rest_framework import serializers
from inventory.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        supplier_name = serializers.ReadOnlyField()
        model = Product
        fields = ['name','supplier_name','availability']




