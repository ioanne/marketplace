from django.urls import path

from transaction.views import TransactionsAPIView


urlpatterns = [
    path("", TransactionsAPIView.as_view(), name="transactions"),
]
