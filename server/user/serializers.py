from rest_framework import serializers
from .models import User, GlobalSettings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserNoPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class UserNoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['type']


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'ac', 'submit', 'desc', 'ac_pid']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class GlobalSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalSettings
        fields = '__all__'
