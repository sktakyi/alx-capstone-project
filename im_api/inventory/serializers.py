from rest_framework import serializers
from .models import Category, Product, Supplier, Inventory, InventoryLog, Customer, Order




# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# Supplier Serializer
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


# Inventory Serializer
class InventorySerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()  # To display product

    class Meta:
        model = Inventory
        fields = '__all__'


# Inventory Log Serializer
class InventoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLog
        fields = '__all__'


# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()  # To display customer name
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())


    class Meta:
        model = Order
        fields = '__all__'
