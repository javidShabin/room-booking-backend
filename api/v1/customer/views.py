from django.http import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from customer.models import Customer

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(email=email, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        response_data = {
            "status_code": 6000,
            "data": {"access": str(refresh.access_token)},
            "message": "Login success",
        }
    else:
        response_data = {"status": 6001, "message": "invalide creadential"}
    return Response(response_data)


# User signup function
@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    first_name = request.data.get("firstName")
    last_name = request.data.get("lastName")
    email = request.data.get("email")
    password = request.data.get("password")
    confirm_password = request.data.get("confirmPassword")
    phone = request.data.get("phone")

    if not all([first_name, last_name, email, password, confirm_password, phone]):
        return Response(
            {"status": 6001, "message": "All fields are required"}, status=400
        )

    if password != confirm_password:
        return Response(
            {"status": 6001, "message": "Password do not match"}, status=400
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {"status": 6001, "message": "Email already exists"},
            status=400,
        )
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        phone=phone,
    )
    user.save()

    customer = Customer.objects.create(user=user)
    customer.save()
    refresh = RefreshToken.for_user(user)

    response_data = {
        "status_code": 6000,
        "data": {"access": str(refresh.access_token)},
        "message": "User signup success",
    }
    return Response(response_data)

# user logout function
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def logout(request):
    return Response({"status": 6000, "message": "User logout success"}, status=200)
