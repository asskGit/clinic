from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer
from doctor.models import Doctor
from django.http import Http404
from datetime import time

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['gender', 'birthday', 'date_of_appointment']

    def get_queryset(self):
        queryset = Patient.objects.all()
        age_min = self.request.query_params.get('age_min', None)
        age_max = self.request.query_params.get('age_max', None)
        if age_min:
            queryset = queryset.filter(age__gte=age_min)
        if age_max:
            queryset = queryset.filter(age__lte=age_max)

        date_of_appointment = self.request.query_params.get('date_of_appointment', None)
        if date_of_appointment:
            queryset = queryset.filter(date_of_appointment=date_of_appointment)

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        return PatientSerializer

    def list_available_time_slots(self, request):
        doctor_id = request.query_params.get('doctor_id')
        date_of_appointment = request.query_params.get('date_of_appointment')

        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            raise Http404("Doctor does not exist")

        existing_appointments = Patient.objects.filter(
            recording=doctor,
            date_of_appointment=date_of_appointment
        ).values_list('time_of_appointment', flat=True)

        all_time_slots = ['09:00-10:00',
                          '10:00', '11:00',
                          '12:00', '13:00',
                          '14:00', '15:00',
                          '16:00', '17:00']

        available_time_slots = [time_slot for time_slot in all_time_slots if time_slot not in existing_appointments]

        return Response(available_time_slots, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

