from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(DoctorService)
admin.site.register(Visit)
