from rest_framework import serializers
from datetime import datetime

class PongSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
    timestamp = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return "Pong!"

    def update(self, instance, validated_data):
        pass

    def to_representation(self, instance):
        return {
            'message': 'Pong!',
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }