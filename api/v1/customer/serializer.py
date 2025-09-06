from rest_framework import serializers
from users.models import User
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = User
        fields= [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'is_customer',
            'is_manager',
            'is_admin',
            'customer'
        ]