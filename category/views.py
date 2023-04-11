from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from category.models import Category
from category.serializers import CategorySerializer



# class CategoryApiView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)


class CategoryApiView(ListAPIView):
    model = Category
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset