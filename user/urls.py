from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='user')
router.register(r'patient', PatientViewSet, basename='patient')

urlpatterns = [
]

urlpatterns += router.urls
