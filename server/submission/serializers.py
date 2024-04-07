from rest_framework import serializers
from .models import SubmissionResult, CaseDetail


class SubmissionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionResult
        exclude = ['code', 'message']


class SubmissionCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmissionResult
        fields = '__all__'


class CaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseDetail
        fields = '__all__'
