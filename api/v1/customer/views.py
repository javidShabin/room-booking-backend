from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from customer.models import Customer
from rest_framework.generics import get_object_or_404
from .serializer import UserProfileSerializer
from rest_framework.parsers import MultiPartParser, FormParser

from django.contrib.auth import authenticate

# **************************************************************************************
# ************************ User authentication functions *******************************


# User login function
# *************************************************
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


# End login function
# **************************************************************************


# User signup function
# ******************************************
@api_view(["POST"])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def signup(request):
    # Get user details from request data
    first_name = request.data.get("firstName")
    last_name = request.data.get("lastName")
    email = request.data.get("email")
    password = request.data.get("password")
    confirm_password = request.data.get("confirmPassword")
    phone = request.data.get("phone")
    profile_image = request.FILES.get("profile_image")
    role = request.data.get("role")  # "customer", "manager", "admin"

    # Check required fields
    if not all(
        [
            first_name,
            last_name,
            email,
            password,
            confirm_password,
            phone,
            profile_image,
            role,
        ]
    ):
        return Response(
            {"status": 6001, "message": "All fields are required"}, status=400
        )

    # Compare passwords
    if password != confirm_password:
        return Response(
            {"status": 6001, "message": "Passwords do not match"}, status=400
        )

    # Check if email already exists
    if User.objects.filter(email=email).exists():
        return Response(
            {"status": 6001, "message": "Email already exists"},
            status=400,
        )

    # Validate role
    if role not in ["customer", "manager", "admin"]:
        return Response({"status": 6001, "message": "Invalid role"}, status=400)

    # Create new user with role-specific flags
    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "profile_image": profile_image,
    }

    if role == "customer":
        user = User.objects.create_user(**user_data, is_customer=True)
        Customer.objects.create(user=user)  # optional if using Customer model
    elif role == "manager":
        user = User.objects.create_user(**user_data, is_manager=True)
    elif role == "admin":
        user = User.objects.create_user(
            **user_data, is_admin=True, is_staff=True, is_superuser=True
        )

    # Generate JWT token
    refresh = RefreshToken.for_user(user)

    # Send response
    response_data = {
        "status_code": 6000,
        "data": {"access": str(refresh.access_token), "role": role},
        "message": "User signup success",
    }
    return Response(response_data)


# End the signup function
# *************************************************************************


# user logout function
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def logout(request):
    return Response({"status": 6000, "message": "User logout success"}, status=200)


# End the user logout function
# ********************************************************


# *************************************************************************************
# **************************** User profile section functions *************************


# Get profil by userId
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user.id != user.id:
        return Response({"status": 6001, "message": "Permission denied"}, status=403)

    serializer = UserProfileSerializer(user)

    response_data = {
        "status_code": 6000,
        "data": serializer.data,
        "message": "User profile fetched successfully",
    }

    return Response(response_data, status=200)


# ******************** User get profile by user id **********************
# ***********************************************************************


# Get the all users list from database
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_users_list(request):
    users = User.objects.all()
    users_data = []
    for user in users:
        users_data.append(
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "phone": user.phone,
                "profile": user.profile_image.url if user.profile_image else None,
            }
        )
    response_data = {
        "status_code": 6000,
        "data": users_data,
        "message": "Get all users list",
    }
    return Response(response_data, status=200)


# ******************** User list function is completed *******************
# ************************************************************************


# ************************************************************************
# ******************** User profile update , Find user by Id *************


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Ensure the user can only update their own profile
    if request.user.id != user.id:
        return Response({"status": 6001, "message": "Permission denied"}, status=403)

    # Extract data from request
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone = request.data.get("phone")
    profile_image = request.FILES.get("profile_image")

    # Update fields if provided
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if phone:
        user.phone = phone

    if profile_image:
        # delete old image file if exists
        if user.profile_image:
            user.profile_image.delete(save=False)
        user.profile_image = profile_image
    user.save()

    serializer = UserProfileSerializer(user)

    response_data = {
        "status_code": 6000,
        "data": serializer.data,
        "message": "User profile updated successfully",
    }
    return Response(response_data, status=200)
