from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PongSerializer

class PongView(APIView):
    def get(self, request):
        serializer = PongSerializer()
        return Response(serializer.to_representation(None))