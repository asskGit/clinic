from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField("Имя", max_length=255)
    last_name = models.CharField("Фамилия", max_length=255)
    email = models.EmailField("Почта", unique=True, blank=True, null=True)
    username = models.CharField(verbose_name="Никнейм", max_length=100, unique=False, null=True, blank=True)
    photo = models.ImageField("Фото", upload_to='user-photo/', blank=True, null=True)
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField("Пол", max_length=255, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], default='Мужской')

    USERNAME_FIELD = "email"  # Установите поле email в качестве уникального идентификатора пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Поля, которые требуются при создании суперпользователя

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email



