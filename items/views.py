from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView

from items.models import Item
from items.serializers import ItemSerializer


class ItemApiView(ListAPIView, CreateAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        return queryset


class SpecificItemApiView(RetrieveAPIView, DestroyAPIView):  
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        return queryset
