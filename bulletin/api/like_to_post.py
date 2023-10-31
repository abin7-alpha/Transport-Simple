import traceback, sys

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from authorization.models import Account

from bulletin.models import Like, Post

@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def like_post(request):
    output = {}
    data = request.data
    try:
        user_id = data['userId']
        post_id = data['postId']
        try:
            user = Account.objects.get(id=user_id)
            post = Post.objects.get(id=post_id)
            try:
                like = Like.objects.create(
                    user=user,
                    post=post
                )
                output['status'] = 'success'
                output['status_text'] = 'Successfully like the post'
                return Response(output, status=status.HTTP_200_OK)
            except:
                traceback.print_exc(file=sys.stdout)
                output['status'] = "failed"
                output['status_text'] = "Failed to like the post"
                return Response(output, status=status.HTTP_501_NOT_IMPLEMENTED)
        except:
            traceback.print_exc(file=sys.stdout)
            output['status'] = "failed"
            output['status_text'] = "Failed to get the user data"
            return Response(output, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Exception as error:
        traceback.print_exc(file=sys.stdout)
        output['status'] = "failed"
        output['status_text'] = f"Ivalid data: {error}"
        return Response(output, status=status.HTTP_400_BAD_REQUEST)
    