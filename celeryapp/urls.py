# app/urls.py
from django.urls import path
from .views import ProductListCreateView, ProductImportExcelView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/import/', ProductImportExcelView.as_view(), name='product-import'),
]
