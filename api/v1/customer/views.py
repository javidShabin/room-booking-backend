from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from customer.models import Customer
from rest_framework.generics import get_object_or_404

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

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
def signup(request):
    # Get user details from request data
    first_name = request.data.get("firstName")
    last_name = request.data.get("lastName")
    email = request.data.get("email")
    password = request.data.get("password")
    confirm_password = request.data.get("confirmPassword")
    phone = request.data.get("phone")
    role = request.data.get("role")  # "customer", "manager", "admin"

    # Check required fields
    if not all([first_name, last_name, email, password, confirm_password, phone, role]):
        return Response(
            {"status": 6001, "message": "All fields are required"},
            status=400
        )

    # Compare passwords
    if password != confirm_password:
        return Response(
            {"status": 6001, "message": "Passwords do not match"},
            status=400
        )

    # Check if email already exists
    if User.objects.filter(email=email).exists():
        return Response(
            {"status": 6001, "message": "Email already exists"},
            status=400,
        )

    # Validate role
    if role not in ["customer", "manager", "admin"]:
        return Response(
            {'status': 6001, 'message':'Invalid role'},
            status=400
        )

    # Create new user with role-specific flags
    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
    }

    if role == "customer":
        user = User.objects.create_user(**user_data, is_customer=True)
        Customer.objects.create(user=user)  # optional if using Customer model
    elif role == "manager":
        user = User.objects.create_user(**user_data, is_manager=True)
    elif role == "admin":
        user = User.objects.create_user(**user_data, is_admin=True, is_staff=True, is_superuser=True)

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

    customer = Customer.objects.filter(user=user).first()

    serializer = UserSerializer
    data = {
        "id": user.id,
        "firstName": user.first_name,
        "lastName": user.last_name,
        "email": user.email,
        "phone": user.phone,
        "isCustomer": user.is_customer,
        "isManager": user.is_manager,
        "customer": {"id": customer.id} if customer else None,
    }

    response_data = {
        "status_code": 6000,
        "data": data,
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
            }
        )
    response_data = {
        'status_code': 6000,
        'data': users_data,
        'message':'Get all users list'
    }
    return Response(response_data, status=200)

# ******************** User list function is completed *******************
# ************************************************************************