from django.contrib import admin
from users.models import User
from customer.models import Customer

admin.site.register(User)
admin.site.register(Customer)
