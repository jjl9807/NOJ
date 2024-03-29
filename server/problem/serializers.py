from rest_framework import serializers
from .models import Problem, ProblemInfo, ProblemTag


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class ProblemInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemInfo
        fields = '__all__'


class ProblemTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemTag
        fields = '__all__'
