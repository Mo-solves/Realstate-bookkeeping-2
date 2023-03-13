from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from .views import (
    CustomerList,
    CustomerDetail,
    CustomerCreate,
    CustomerUpdate,
    RealStateList,
    RealStateDetail,
)

urlpatterns = [
    path("customer/list/", CustomerList.as_view(), name="customer-list"),
    path("customer/add-customer/", CustomerCreate.as_view(), name="add-customer"),
    path("customer/<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
    path("customer/update/<int:pk>/", CustomerUpdate.as_view(), name="customer-update"),
    path("realstate/list/", RealStateList.as_view(), name="realstate-list"),
    path("realstate/<int:pk>/", RealStateDetail.as_view(), name="realstate-detail"),
]
