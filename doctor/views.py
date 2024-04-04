from rest_framework import viewsets, status
from .models import Tag, Doctor
from .serializers import TagSerializer, DoctorSerializer, DoctorManualSerializer
from rest_framework.response import Response
from user.models import User


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def list(self, request, *args, **kwargs):
        doctors = Doctor.objects.all()
        data = []
        for doctor in doctors:
            data.append({
                "id": doctor.id,
                "Имя": f"{doctor.doctor.first_name} {doctor.doctor.last_name}",
                "Email": doctor.doctor.email,
                "Теги": doctor.tag.name,
                "Клиенты": doctor.client
            })
        return Response(data)

    def create(self, request, *args, **kwargs):
        username = request.data["username"]
        birthday = request.data["birthday"]
        tag_request = request.data["tag"]
        gender = request.data["gender"]
        email = request.data["email"]
        address = request.data["address"]
        login = request.data["login"]
        password = request.data["password"]
        client = request.data['client']

        gender = "Мужской" if gender == "M" else "Женский"
        first_name = username.split()[0]
        last_name = username.split()[1]

        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=login,
                                   birthday=birthday, gender=gender,  password=password)
        tag = Tag.objects.filter(id=int(tag_request)).first()
        Doctor.objects.create(doctor=user, tag=tag, client=client, address=address)
        return Response("Доктор Успешно добавлен!")

    def retrieve(self, request, *args, **kwargs):
        doctor = Doctor.objects.get(id=int(kwargs['pk']))
        data = {
            "id": doctor.id,
            "Имя": f"{doctor.doctor.first_name} {doctor.doctor.last_name}",
            "Дата рождения": doctor.doctor.birthday,
            "Email": doctor.doctor.email,
            "Теги": doctor.tag.name,
            "Пол": doctor.doctor.gender,
            "Адрес": doctor.address,
        }
        return Response(data)

    def destroy(self, request, *args, **kwargs):
        Doctor.objects.get(id=kwargs['pk']).delete()
        return Response("Delete")

    def update(self, request, *args, **kwargs):
        doctor_instance = self.get_object()
        user_instance = doctor_instance.doctor

        user_instance.first_name = request.data.get("first_name", user_instance.first_name)
        user_instance.last_name = request.data.get("last_name", user_instance.last_name)
        user_instance.email = request.data.get("email", user_instance.email)
        user_instance.birthday = request.data.get("birthday", user_instance.birthday)
        user_instance.gender = request.data.get("gender", user_instance.gender)
        user_instance.save()

        serializer = DoctorManualSerializer(doctor_instance, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            serializer.save()
            return Response("Update successful")
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        doctor_instance = self.get_object()
        user_instance = doctor_instance.doctor

        user_instance.first_name = request.data.get("first_name", user_instance.first_name)
        user_instance.last_name = request.data.get("last_name", user_instance.last_name)
        user_instance.email = request.data.get("email", user_instance.email)
        user_instance.birthday = request.data.get("birthday", user_instance.birthday)
        user_instance.gender = request.data.get("gender", user_instance.gender)
        user_instance.save()

        serializer = DoctorManualSerializer(doctor_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Partial update successful")
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DoctorManualSerializer
        return self.serializer_class