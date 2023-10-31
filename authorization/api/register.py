import traceback, sys

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from authorization.models import Account
from authorization.functions import get_token
from authorization.serializers.account import AccountSerializer


@api_view(['POST'])
@permission_classes([AllowAny,])
def register_user(request):
    data = request.data
    output = {}
    try:
        firstname = data['firstName']
        lastname = data['lastName']
        email = data['email']
        password = data['password']
        contact_no = data['contactNo']
        role = data['role']
        try:

            account = Account.objects.create(
                role=role,
                contact_number=contact_no,
                first_name=firstname,
                last_name=lastname,
                email=email,
                is_active=True
            )

            account.set_password(password)
            account.save()
            
            try:
                redirect_uri = 'http://127.0.0.1:8000/'
                token = get_token(email, password, redirect_uri)
                account_serializer = AccountSerializer(account)
                output['status'] = 'success'
                output["status_text"] = "Succesfully Auntheticated"
                output["email"] = account.email
                output['user'] = f'{account.first_name} {account.last_name}'
                output['contact_no'] = account.contact_number
                output.update(token)
                return Response(output, status=status.HTTP_200_OK)
            except:
                traceback.print_exc(file=sys.stdout)
                output['status'] = "failed"
                output['status_text'] = "Failed to generate token"
                return Response(output, status=status.HTTP_400_BAD_REQUEST)
        except:
            traceback.print_exc(file=sys.stdout)
            output['status'] = "failed"
            output['status_text'] = "Failed to register the user"
            return Response(output, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        traceback.print_exc(file=sys.stdout)
        output['status'] = "failed"
        output['status_text'] = f"Ivalid data: {error}"
        return Response(output, status=status.HTTP_400_BAD_REQUEST)

