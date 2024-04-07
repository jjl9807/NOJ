from rest_framework import serializers
from .models import User, UserStatus, UserLoginRecord, GlobalSettings


class UserLoginRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLoginRecord
        fields = '__all__'


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
        model = UserStatus
        fields = '__all__'


class GlobalSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalSettings
        fields = '__all__'
