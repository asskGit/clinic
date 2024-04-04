from rest_framework import serializers
from .models import *
from doctor.models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'photo', 'birthday', 'gender')


