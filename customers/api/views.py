from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from customers.models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    def retreive(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    # def create(self, request):
    #     serializer = CustomerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             {"message": "Customer created"}, status=status.HTTP_201_CREATED
    #         )
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, pk):
    #     customer = Customer.objects.get(pk=pk)
    #     customer.delete()
    #     return Response(
    #         {"message": "customer deleted"}, status=status.HTTP_204_NO_CONTENT
    #     )
