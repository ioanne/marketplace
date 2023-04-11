from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView

from transaction.models import Transaction
from transaction.serializers import TransactionSerializer

class TransactionsAPIView(ListAPIView, CreateAPIView):
    model = Transaction
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        return queryset



"""
    ListApiView:
        Es una clase en django que nos permite
        listar objetos de la base de datos.

    CreateAPIView:
        Es una clase en django que nos permite
        crear objetos en la base de datos.

"""