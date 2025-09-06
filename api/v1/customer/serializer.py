from rest_framework import serializers
from users.models import User
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id']

class UserProfileSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    isCustomer = serializers.BooleanField(source='is_customer')
    isManager = serializers.BooleanField(source='is_manager')
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'firstName',
            'lastName',
            'email',
            'phone',
            'isCustomer',
            'isManager',
            'customer',
        ]