from urllib import response
from django.core.serializers import serialize
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

from api.v1 import hotel
from .serializer import HotelSerializer
from hotel.models import Hotel

# **************************************************************
# **************** CURD operations of hotel ********************


# Create Hotel
# ************************
@api_view(["POST"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def create_hotel(request):
    name = request.data.get("name")
    location = request.data.get("location")
    manager_id = request.data.get("manager_id") or request.data.get("managerId")
    if not manager_id:
        return Response(
            {"status": 6001, "message": "manager_id is required"}, status=400
        )
    if (
        name
        and location
        and Hotel.objects.filter(name=name, location=location).exists()
    ):
        return Response({"status": 6001, "message": "Hotel already exists"}, status=400)
    data = request.data.copy()
    data["manager_id"] = manager_id
    serializer = HotelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        response_data = {
            "status_code": 6000,
            "data": serializer.data,
            "message": "Hotel created successfully",
        }
        return Response(response_data, status=201)
    return Response({"status": 6001, "errors": serializer.errors}, status=400)


# Get all hotels list
# *********************************
@api_view(["GET"])
@permission_classes([AllowAny])
def get_hotels_list(request):
    hotels = Hotel.objects.all()
    for user in hotels:
        serializer = HotelSerializer(hotels, many=True)
        response_data = {
            "status_code": 6000,
            "data": serializer.data,
            "message": "Hotels fetched successfully",
        }
        return Response(response_data, status=200)


# Get hotel by id
# *********************************
@api_view(["GET"])
@permission_classes([AllowAny])
def single_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    serializer = HotelSerializer(hotel)

    response_data = {
        "status_code": 6000,
        "data": serializer.data,
        "message": "Hotel fetched successfully",
    }

    return Response(response_data, status=200)


# ************ Admin can activate the hotels after verification ********
# **********************************************************************
@api_view(["POST"])
@permission_classes([IsAuthenticated])  # User must be authenticated
def activate_hotel(request, hotel_id):
    if not (request.user.is_customer or request.user.is_manager):
        return Response({"status": 6001, "message": "Permission denied"}, status=403)

    hotel = get_object_or_404(Hotel, id=hotel_id)
    hotel.is_active = True
    hotel.save()

    serializer = HotelSerializer(hotel)

    response_data = {
        "status_code": 6000,
        "data": serializer.data,
        "message": "Hotel activated successfully",
    }

    return Response(response_data, status=200)
