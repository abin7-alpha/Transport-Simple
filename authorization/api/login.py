import traceback, sys
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import api_view, permission_classes

from authorization.models import Account
from authorization.functions import get_token


@api_view(['POST',])
@permission_classes([AllowAny,])
def login_user(request):
    data = request.data
    output = {}

    email = data['email']
    password = data['password']

    try:
        account = Account.objects.get(email=email)
    except:
        traceback.print_exc(file=sys.stdout)
        output['status'] = "failed"
        output['status_text'] = "Account not exists"
        return Response(output, status=status.HTTP_404_NOT_FOUND)

    try:
        if account.is_active:
            pass
        else:
            raise Exception
    except:
        output['status'] = "failed"
        output['status_text'] = "Your account has been inactive, contact admin"
        return Response(output, status=status.HTTP_400_BAD_REQUEST)

    try:
        try:
            authorized_user = authenticate(request, username=email, password=password)

            if authorized_user == None:
                raise Exception
        except:
            output['status'] = "failed"
            output['status_text'] = "Incorrect password"
            return Response(output, status=status.HTTP_401_UNAUTHORIZED)
        
        redirect_uri = 'http://127.0.0.1:8000/'
        token = get_token(email, password, redirect_uri)
        output['status'] = 'success'
        output["status_text"] = "Succesfully Auntheticated"
        output["email"] = account.email
        output['user'] = f'{account.first_name} {account.last_name}'
        output['user_id'] = account.id
        output['contact_no'] = account.contact_number
        output['is_active'] = account.is_active
        output.update(token)
        return Response(output, status=status.HTTP_200_OK)
    except Exception as error:
        traceback.print_exc(file=sys.stdout)
        output['status'] = "failed"
        output['status_text'] = "Failed to login"
        return Response(output, status=status.HTTP_400_BAD_REQUEST)
