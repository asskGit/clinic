from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'', DoctorViewSet, basename='doctor')
router.register(r'tag', TagViewSet, basename='tag')

urlpatterns = [
]

urlpatterns += router.urls
