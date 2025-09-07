from django.db import models
from django.contrib.auth.models import AbstractUser

from users.manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, max_length=256, error_messages={"unique": "Email already existes"}
    )
    phone = models.CharField(max_length =10 )
    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_images/',
    blank=True,
    null=True,
    max_length=300,  # Increased from default 100
    default='https://img.freepik.com/premium-vector/avatar-profile-picture-icon-gray-background-flat-design-style-resources-graphic-element-design_991720-445.jpg?semt=ais_incoming&w=740&q=80')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "Users_user"
        verbose_name = "Users"
        verbose_name_plural = "Users"
        ordering = ["-id"]

    def _str_(self):
        return self.email
