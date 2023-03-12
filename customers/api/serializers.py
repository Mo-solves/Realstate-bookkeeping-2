from rest_framework import serializers
from customers.models import Customer, RealState


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class RealStateSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()

    class Meta:
        model = RealState
        fields = ["customer", "location"]
