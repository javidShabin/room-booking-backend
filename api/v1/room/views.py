from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser

from .serializer import RoomSerializer
from room.models import Room


# **********************************************************************************
# ************************* CRUD operations for rooms ******************************

# Create Room by hotel id