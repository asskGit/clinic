from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorManualSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    birthday = serializers.DateField(write_only=True, required=True)
    gender = serializers.ChoiceField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], default='Мужской')
    email = serializers.EmailField(write_only=True, required=True)
    login = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Doctor
        fields = ('username', 'birthday', 'tag', 'gender', 'email', 'address', 'login', 'password', 'client')
