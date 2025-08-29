from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate ,login as auth_login, logout as auth_logout

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(email = email , password = password)
    if user:
        refresh = RefreshToken.for_user(user)
        response_data = {
            'status_code': 6000,
            'data': {
                'access': str(refresh.access_token)
            },
            'message':"Login success"
        }
    else:
        response_data = {
            'status': 6001,
            'message': 'invalide creadential'
        }
    return Response(response_data)