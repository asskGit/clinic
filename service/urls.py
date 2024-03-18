from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'', ServiceViewSet, basename='service')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'doctor_service', DoctorServiceViewSet, basename='doctor_service')
router.register(r'visit', VisitViewSet, basename='visit')

urlpatterns = [
]

urlpatterns += router.urls
