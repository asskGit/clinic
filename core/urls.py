
from django.contrib import admin
from django.urls import path, include
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from patient.views import *
from branch.views import *
from doctor.views import *
from service.views import *
from user.views import *

router = DefaultRouter()
router.register(r'patient', PatientViewSet)
router.register(r'branch', BranchViewSet)
router.register(r'doctor', DoctorViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'user', UserViewSet)



urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path('admin/', admin.site.urls),
    path('docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path('', include(router.urls)),
]
