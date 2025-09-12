from django.contrib import admin
from users.models import User
from customer.models import Customer
from hotel.models import Hotel

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Hotel)
