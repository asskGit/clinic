from django.db import models
from user.models import User


class Tag(models.Model):
    name = models.CharField("Тег", max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    doctor = models.OneToOneField(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, related_name="doctor_tag")
    address = models.CharField(max_length=255, default="")
    description = models.TextField(blank=True)
    experience = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.doctor.__str__()
