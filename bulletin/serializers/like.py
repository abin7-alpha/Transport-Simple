from bulletin.models import Like
from rest_framework import serializers

class LikeSerializer(serializers.Serializer):
    class Meta:
        model = Like
        fields = '__all__'
        depth = 2
        