from django.urls import path

from .views import ProductListView, product_list_json


urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("api/products/", product_list_json, name="product-list-json"),
]
