from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProductViewSet, SupplierViewSet,
    CustomerViewSet, OrderViewSet, InventoryViewSet, InventoryLogViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'inventory-log', InventoryLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]