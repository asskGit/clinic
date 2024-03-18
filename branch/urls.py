from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'', BranchViewSet, basename='branch')

urlpatterns = [
]

urlpatterns += router.urls
