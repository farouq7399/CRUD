from django.contrib import admin
from django.urls import path, include
from .views import ProductList, UsersList, CreateProduct, detailsProduct

urlpatterns = [
    path('list/', ProductList.as_view(), name="list"),
    path('list_user/', UsersList.as_view()),
    path('create_product/', CreateProduct.as_view(), name="create_product"),
    path('details_product/<int:pk>', detailsProduct.as_view(), name="details_product"),
]
