# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import ContestAnnouncement, ContestBoard, ContestInfo, ContestProblem, ContestPlayer, ContestBoardTotal


class ContestAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestAnnouncement
        fields = '__all__'


class ContestBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestBoard
        fields = '__all__'


class ContestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestInfo
        fields = '__all__'


class ContestProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestProblem
        fields = '__all__'


class ContestPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestPlayer
        fields = '__all__'


class ContestBoardTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestBoardTotal
        fields = '__all__'
