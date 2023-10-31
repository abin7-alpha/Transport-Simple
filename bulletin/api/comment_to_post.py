import traceback, sys

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from authorization.models import Account

from bulletin.models import Comment, Post

@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def create_comment(request):
    output = {}
    data = request.data
    try:
        user_id = data['userId']
        comment = data['comment']
        post_id = data['postId']
        try:
            user = Account.objects.get(id=user_id)
            post = Post.objects.get(id=post_id)
            try:
                comment = Comment.objects.create(
                    author=user,
                    content=comment,
                    post=post
                )
                output['status'] = 'success'
                output['status_text'] = 'Successfully created the comment'
                return Response(output, status=status.HTTP_200_OK)
            except:
                traceback.print_exc(file=sys.stdout)
                output['status'] = "failed"
                output['status_text'] = "Failed to create the comment"
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
    