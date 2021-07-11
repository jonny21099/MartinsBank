from rest_framework import viewsets
from rest_framework.response import Response

from .models import Account

from .serializer import AccountSerializer


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('card_number')
    serializer_class = AccountSerializer

    def list(self, request, *args, **kwargs):
        queryset = Account.objects.filter(user_id=kwargs['id'])
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)


class AccountsView(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('card_number')
    serializer_class = AccountSerializer
