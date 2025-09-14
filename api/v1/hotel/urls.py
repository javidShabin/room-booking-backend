from django.urls import path
from api.v1.hotel import views

app_name = "hotel"

urlpatterns = [
    path("create/", views.create_hotel, name="create_hotel"),
    path("hotel_list/", views.get_hotels_list, name="hotel_list"),
    path("single_hotel/<int:hotel_id>/", views.single_hotel, name="single_hotel"),
    path("activate/<int:hotel_id>/", views.activate_hotel, name="activate_hotel"),
  
]
