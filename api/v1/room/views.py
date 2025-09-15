from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

from .serializer import RoomSerializer
from room.models import Room
from hotel.models import Hotel


# **********************************************************************************
# ************************* CRUD operations for rooms ******************************

# Create Room by hotel id
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_room(request):
    hotel_id = request.data.get("hotel_id")
    hotel = get_object_or_404(Hotel, id=hotel_id)
    
    data = request.data.copy()
    data['hotel'] = hotel.id  # Assuming Room has hotel ForeignKey
    
    serializer = RoomSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": 200, "message": "Room created", "room": serializer.data})
    return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})
# Get all rooms by hotel id
# Update room by id
# Delete room by id
# Change the room status