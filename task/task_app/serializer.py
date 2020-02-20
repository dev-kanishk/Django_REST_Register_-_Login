from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import bios
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class BioSerializer(serializers.ModelSerializer):
    phone_no = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=bios.objects.all())]
            )

    def save(self):
        ph = bios(phone_no = self.validated_data['phone_no'],username = self.validated_data['username'])
        ph.save()


    class Meta:
        model = bios
        fields = ('phone_no','username')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=200)

class InfoSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    phone_no = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)


class customError(serializers.Serializer):
    msg = serializers.CharField(max_length=100)
    