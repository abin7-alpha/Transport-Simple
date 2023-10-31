from bulletin.models import Post
from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ['comments', 'likes', 'title', 'content', 'created_by', 'created']
        depth = 2
        