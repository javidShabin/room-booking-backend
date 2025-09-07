
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/customer/',include("api.v1.customer.urls",namespace='customer')),
]
