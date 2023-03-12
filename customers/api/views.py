from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


from customers.models import Customer, RealState
from .serializers import CustomerSerializer, RealStateSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class RealStateList(generics.ListCreateAPIView):
    queryset = RealState.objects.all()
    serializer_class = RealStateSerializer


class RealStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RealState.objects.all()
    serializer_class = RealStateSerializer
