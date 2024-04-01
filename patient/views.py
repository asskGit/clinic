from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Patient
from .serializers import *
from datetime import datetime, time, timedelta
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



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

        # Добавляем фильтрацию по дате записи пациентов
        date_of_appointment = self.request.query_params.get('date_of_appointment', None)
        if date_of_appointment:
            queryset = queryset.filter(date_of_appointment=date_of_appointment)

        return queryset


    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        return PatientSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def update(self, request, pk=None):
        queryset = self.get_queryset()
        patient = queryset.filter(pk=pk).first()
        if patient:
            serializer = self.serializer_class(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        queryset = self.get_queryset()
        patient = queryset.filter(pk=pk).first()
        if patient:
            serializer = self.serializer_class(patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        patient = queryset.filter(pk=pk).first()
        if patient:
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Patient not found", status=status.HTTP_404_NOT_FOUND)

