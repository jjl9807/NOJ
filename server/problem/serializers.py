from rest_framework import serializers
from .models import Problem, ProblemMeta, ProblemTag


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class ProblemMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemMeta
        fields = '__all__'


class ProblemTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemTag
        fields = '__all__'
