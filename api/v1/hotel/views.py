from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
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
    if name and location and Hotel.objects.filter(name=name, location=location).exists():
        return Response({"status": 6001, "message": "Hotel already exists"}, status=400)
    serializer = HotelSerializer(data=request.data)
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