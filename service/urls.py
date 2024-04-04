from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'', ServiceViewSet, basename='service')
router.register(r'category', CategoryViewSet, basename='category')


urlpatterns = [
]

urlpatterns += router.urls
