from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView

from category.models import Category
from category.serializers import CategorySerializer



class SpecificCategoryApiView(RetrieveAPIView, DestroyAPIView):  
    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class CategoryApiView(ListAPIView, CreateAPIView):
    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset
