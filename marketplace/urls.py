"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path as url

API_VERSION = "v1"
BASE_URL = f"api/{API_VERSION}/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{BASE_URL}" + "items/", include("items.urls")),
    path(f"{BASE_URL}" + "category/", include("category.urls")),
    path(f"{BASE_URL}" + "transactions/", include("transaction.urls")),
]
