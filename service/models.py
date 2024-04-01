from django.db import models
from doctor.models import Doctor


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='services/')
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class DoctorService(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_service')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='doctor_service')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.doctor.__str__()} - {self.service.__str__()}"


status_choices = {
    'Новый': 'Новый',
    'В ожидании': 'В ожидании',
    'Отменено': 'Отменено',
    'Завершено': 'Завершено',
}


class Visit(models.Model):
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=status_choices.items(), default='Новый')
    complaints = models.TextField(max_length=255)
    start = models.DateTimeField(default='', blank=True)
    duration = models.PositiveIntegerField(default=0, blank=True)
    is_active_visit = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient.__str__()} - {self.doctor.__str__()}"

