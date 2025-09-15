from rest_framework import serializers
from room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "hotel_id",
            "number",
            "floor",
            "room_type",
            "description",
            "price",
            "is_available",
            "image",
            "status",
            "capacity",
            "created_at",
            "updated_at",
        ]
