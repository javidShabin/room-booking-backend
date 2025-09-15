from django.contrib import admin
from users.models import User
from customer.models import Customer
from hotel.models import Hotel
from room.models import Room

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Hotel)
admin.site.register(Room)