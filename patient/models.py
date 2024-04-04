from django.db import models
from doctor.models import Doctor
from datetime import datetime, time
from django.utils import timezone


class Patient(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField("Пол", max_length=255, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')],
                              default='Мужской')
    address = models.CharField(max_length=255, default='Derjinka')
    phone_number = models.CharField(max_length=55, default='+996709706065')
    complaints = models.TextField(blank=True, null=True)
    recording = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date_of_appointment = models.DateField("Дата записи", null=True, blank=True)
    time_of_appointment = models.TimeField("Время записи", null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}"

    @staticmethod
    def get_available_time_slots(doctor_id, date_of_appointment):
        doctor = Doctor.objects.get(id=doctor_id)
        existing_appointments = Patient.objects.filter(recording=doctor, date_of_appointment=date_of_appointment)

        all_time_slots = [
            time(hour) for hour in range(8, 18)
        ]  # Генерируем список временных слотов с 9:00 до 17:00

        busy_time_slots = [
            appointment.time_of_appointment for appointment in existing_appointments
        ]  # Получаем список временных слотов, уже занятых записями

        available_time_slots = [
            time_slot for time_slot in all_time_slots if time_slot not in busy_time_slots
        ]  # Отфильтровываем свободные временные слоты

        return available_time_slots
