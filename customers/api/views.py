from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from django.http import Http404
from datetime import timedelta, date


from customers.models import Customer, RealState
from .serializers import CustomerSerializer, RealStateSerializer


class UpdateCustomerData:
    def update_customer_data(self, customer):
        if customer.remainig_days < 1:
            customer.starting_date = customer.due_date
            customer.due_date = customer.due_date + timedelta(days=30)
            customer.balance += customer.rent_due
            customer.rent_paid = 0
            customer.remainig_days = (customer.due_date - date.today()).days
        return customer


class CustomerList(APIView, UpdateCustomerData):
    """List all customers"""

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(self.update_customer_data(customers), many=True)
        return Response(serializer.data)


class CustomerCreate(APIView):
    """Create a new customer"""

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerUpdate(APIView):
    """Update an existing customer"""

    def get_object(self, pk):
        """Returns the Customer Object"""
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        customer = self.get_object(pk)

        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView, UpdateCustomerData):
    def get_object(self, pk):
        """Returns the Customer Object"""
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(self.update_customer_data(customer))
        return Response(serializer.data)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RealStateList(generics.ListCreateAPIView):
    queryset = RealState.objects.all()
    serializer_class = RealStateSerializer


class RealStateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RealState.objects.all()
    serializer_class = RealStateSerializer
