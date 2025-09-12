from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from .serializer import HotelSerializer

# **************************************************************
# **************** CURD operations of hotel ********************

# Create Hotel
# ************************
@api_view(["POST"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def create_hotel(request):
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
