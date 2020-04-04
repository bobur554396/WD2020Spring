from django.urls import path

from api.views import category_list, category_detail

urlpatterns = [
    path('categories/', category_list),

    path('categories/<int:category_id>/', category_detail),

    # path('categories/<int:category_id>/products/', category_products),
]
