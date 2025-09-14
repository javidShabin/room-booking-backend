from django.urls import path
from api.v1.hotel import views

app_name = "hotel"

urlpatterns = [
    # Create hotel api url
    path("create/", views.create_hotel, name="create_hotel"),
    # Get all hotel api url
    path("hotel_list/", views.get_hotels_list, name="hotel_list"),
    # Get single hotel by ID url
    path("single_hotel/<int:hotel_id>/", views.single_hotel, name="single_hotel"),
    # Activate api url
    path("activate/<int:hotel_id>/", views.activate_hotel, name="activate_hotel"),
    # Update the hotel by id
    path("update_hotel/<int:hotel_id>/", views.update_hotel, name="hotel_update")
  
]
