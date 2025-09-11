from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser

from users.manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, max_length=256, error_messages={"unique": "Email already existes"}
    )
    phone = models.CharField(max_length=10)
    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    profile_image = models.FileField(
        default="https://www.dreamstime.com/illustration/placeholder-profile.html",
        upload_to="profiles/",
        blank=True,
        null=True,
    )

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
