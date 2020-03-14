from django.urls import path

from core.views import product_list, product_detail

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
]
