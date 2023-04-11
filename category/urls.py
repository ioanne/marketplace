from django.urls import path

from category.views import CategoryApiView, SpecificCategoryApiView


urlpatterns = [
    path("", CategoryApiView.as_view(), name="categories"),
    path("<int:pk>/", SpecificCategoryApiView.as_view(), name="get_category"),
]
