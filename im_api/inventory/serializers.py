from rest_framework import serializers
from .models import Category, Product, Supplier, Inventory, InventoryFilter, InventoryLog, Customer, Order




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
    product_name = serializers.StringRelatedField(source='product.name')
    product_category = serializers.StringRelatedField(source='product.category.name')
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2)

    class Meta:
        model = Inventory
        fields = ['product_name', 'product_category', 'product_price', 'quantity', 'last_updated']
from django_filters import rest_framework as filters
from .models import Inventory


class InventoryFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='product__category__name', lookup_expr='icontains')
    price_min = filters.NumberFilter(field_name='product__price', lookup_expr='gte')
    price_max = filters.NumberFilter(field_name='product__price', lookup_expr='lte')
    low_stock = filters.BooleanFilter(method='filter_low_stock')

    class Meta:
        model = Inventory
        fields = ['category', 'price_min', 'price_max', 'low_stock']

    def filter_low_stock(self, queryset, name, value):
        if value:
            return queryset.filter(quantity__lt=10)  # You can define your threshold for "low stock"
        return queryset


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
