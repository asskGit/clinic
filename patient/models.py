from django.db import models

from doctor.models import Doctor


class Patient(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField("Пол", max_length=255, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], default='Мужской')
    address = models.CharField(max_length=255, default='Derjinka')
    phone_number = models.CharField(max_length=55, default='+996709706065')
    complaints = models.TextField(blank=True, null=True)
    recording = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='recording')
    date_of_appointment = models.DateField("Дата записи", null=True, blank=True)
    time_of_appointment = models.TimeField("Время записи", null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}"
