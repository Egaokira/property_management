from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet ,TenantViewSet, RentalPaymentViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'tenants', TenantViewSet)
router.register(r'payments', RentalPaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]