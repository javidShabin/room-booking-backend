from django.urls import path

from api.v1.hotel.views import create_hotel

app_name = "hotel"

urlpatterns = [
    path("create/", create_hotel, name="create_hotel")
  
]
