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

# Create Room
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_room(request):
    hotel_id = request.data.get("hotel_id")
    if not hotel_id:
        return Response({"status": 400, "message": "hotel_id is required"})
    
    hotel = get_object_or_404(Hotel, id=hotel_id)
    data = request.data.copy()
    data['hotel_id'] = hotel.id
    
    serializer = RoomSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": 200, "message": "Room created", "room": serializer.data})
    return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})


# Get all rooms by hotel
@api_view(['GET'])
@permission_classes([AllowAny])
def get_rooms_by_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    rooms = Room.objects.filter(hotel_id=hotel)
    serializer = RoomSerializer(rooms, many=True)
    return Response({"status": 200, "rooms": serializer.data})


# Get single room by id
@api_view(['GET'])
@permission_classes([AllowAny])
def get_room_by_id(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    serializer = RoomSerializer(room)
    return Response({"status": 200, "room": serializer.data})


# Update room by id
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    serializer = RoomSerializer(room, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": 200, "message": "Room updated", "room": serializer.data})
    return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})


# Delete room by id
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    return Response({"status": 200, "message": "Room deleted"})


# Change the room status
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def change_room_status(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    is_available = request.data.get('is_available')
    if is_available is not None:
        room.is_available = is_available
        room.save()
        serializer = RoomSerializer(room)
        return Response({"status": 200, "message": "Room status updated", "room": serializer.data})
    return Response({"status": 400, "message": "is_available field is required"})