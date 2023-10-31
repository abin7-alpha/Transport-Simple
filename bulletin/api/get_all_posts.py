import traceback, sys

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from bulletin.models import Post
from bulletin.serializers.post import PostSerializer

@api_view(['GET',])
@permission_classes([AllowAny,])
def get_all_the_posts(request):
    output = {}
    try:
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        output['status'] = 'success'
        output['status_text'] = 'Successfully fetched all the posts'
        output['posts'] = serializer.data
        return Response(output, status=status.HTTP_200_OK)
    except:
        traceback.print_exc(file=sys.stdout)
        output['status'] = "failed"
        output['status_text'] = "Failed to get the posts"
        return Response(output, status=status.HTTP_400_BAD_REQUEST)
