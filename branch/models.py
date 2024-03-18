from django.db import models
from user.models import User


class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default="Derjinka")
    phone_number = models.CharField(max_length=55, default="+996909909909")
    director = models.ForeignKey(User, on_delete=models.PROTECT, related_name="branch_user")

    def __str__(self):
        return f"{self.name} - {self.address}"
