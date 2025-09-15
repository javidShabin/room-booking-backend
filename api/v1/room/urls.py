from django.urls import path
from api.v1.room import views

app_name = "room"

urlpatterns = [
    path('create/', views.create_room, name="create_room"),
    path('hotel/<int:hotel_id>/', views.get_rooms_by_hotel, name="get_rooms_by_hotel"),
    path('<int:room_id>/', views.get_room_by_id, name="get_room_by_id"),
    path('update/<int:room_id>/', views.update_room, name="update_room"),
    path('delete/<int:room_id>/', views.delete_room, name="delete_room"),
    path('status/<int:room_id>/', views.change_room_status, name="change_room_status"),
]