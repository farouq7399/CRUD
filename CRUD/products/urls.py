from django.contrib import admin
from django.urls import path, include
from .views import ProductList, UsersList, CreateProduct

urlpatterns = [
    path('list/', ProductList.as_view()),
    path('list_user/', UsersList.as_view()),
    path('create_product/', CreateProduct.as_view()),
]
