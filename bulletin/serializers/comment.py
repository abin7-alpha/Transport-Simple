from bulletin.models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 2
        