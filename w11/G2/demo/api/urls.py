from django.urls import path

from api.views import categories_list, category_detail, category_products

urlpatterns = [
    path('categories/', categories_list),
    path('categories/<int:category_id>/', category_detail),
    path('categories/<int:category_id>/products/', category_products),
]
