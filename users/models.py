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
