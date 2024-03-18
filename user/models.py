from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField("Email Address", unique=True, blank=True, null=True)
    username = models.CharField(verbose_name="Username", max_length=100, unique=True, null=True, blank=True)
    avatar = models.ImageField("Avatar", upload_to='users-avatar/', blank=True, null=True)
    birthday = models.DateField("Birth Day", null=True, blank=True)
    gender = models.CharField(max_length=255, choices=[('M', 'Male'), ('F', 'Female')], default='M')

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.get_username()
