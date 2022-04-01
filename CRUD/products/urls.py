from django.contrib import admin
from django.urls import path, include
from .views import ProductList, CreateProduct, detailsProduct, DeleteProduct

urlpatterns = [
    path('list/', ProductList.as_view(), name="list"),
    path('create_product/', CreateProduct.as_view(), name="create_product"),
    path('details_product/<int:pk>', detailsProduct.as_view(), name="details_product"),
    path('details_product/<int:pk>', detailsProduct.as_view(), name="details_product"),
    path('delete_product/<int:pk>', DeleteProduct.as_view(), name="delete_product"),
]
