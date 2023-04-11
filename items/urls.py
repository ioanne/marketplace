from django.urls import path

from items.views import ItemApiView


urlpatterns = [
    path("", ItemApiView.as_view(), name="items"),
]
