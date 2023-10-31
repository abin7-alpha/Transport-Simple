from authorization.models import Account
from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'is_active']
        depth = 1