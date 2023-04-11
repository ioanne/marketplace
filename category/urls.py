from django.urls import path

from category.views import CategoryApiView


urlpatterns = [
    path("", CategoryApiView.as_view(), name="categories"),
]
