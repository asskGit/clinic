from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
]

urlpatterns += router.urls
