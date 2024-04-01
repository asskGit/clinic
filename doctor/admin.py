from django.contrib import admin
from .models import Doctor, Tag


admin.site.register(Tag)
admin.site.register(Doctor)
