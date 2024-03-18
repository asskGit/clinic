from rest_framework import viewsets
from .models import Category, Service, DoctorService, Visit
from .serializers import CategorySerializer, ServiceSerializer, DoctorServiceSerializer, VisitSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class DoctorServiceViewSet(viewsets.ModelViewSet):
    queryset = DoctorService.objects.all()
    serializer_class = DoctorServiceSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
