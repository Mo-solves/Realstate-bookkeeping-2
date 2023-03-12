from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from .views import CustomerList, CustomerDetail, RealStateList, RealStateDetail

urlpatterns = [
    path("customer/list/", CustomerList.as_view(), name="customer-list"),
    path("customer/<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
    path("realstate/list/", RealStateList.as_view(), name="realstate-list"),
    path("realstate/<int:pk>/", RealStateDetail.as_view(), name="realstate-detail"),
]
