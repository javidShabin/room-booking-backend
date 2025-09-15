from django.db import models

class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('deluxe', 'Deluxe'),
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('maintenance', 'Under Maintenance'),
        ('out_of_service', 'Out of Service'),
    ]
    hotel_id = models.ForeignKey('hotel.Hotel', on_delete=models.CASCADE, related_name='rooms')
    number = models.CharField(max_length=10, unique=True)  # Room number
    floor = models.IntegerField()                        # Floor number
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)  # Additional details
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Room price
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)  # Room image
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    capacity = models.IntegerField(default=1)             # Max occupants
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number