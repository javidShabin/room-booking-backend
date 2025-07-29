from django.urls import path
from api.v1.customer import views

app_name = "customer"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("users/", views.get_users_list, name="users_list"),
    path("user/<int:user_id>/", views.get_user_profile, name="user_profile"),
]
