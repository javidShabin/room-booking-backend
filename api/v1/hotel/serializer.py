from rest_framework import serializers
from hotel.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = [
            'id',
            'manager_id',
            'name',
            'location',
            'address',
            'description',
            'rating',
            'number_of_rooms',
            'phone',
            'email',
            'website',
            'is_active',
            'main_image',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


