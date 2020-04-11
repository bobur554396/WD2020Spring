from django.urls import path

# from api.views import category_list, category_detail
# from api.views.views_cbv import CategoryListAPIView, CategoryDetailAPIView
from api.views.views_generic import CategoryListAPIView, CategoryDetailAPIView, \
    ProductListAPIView, ProductDetailAPIView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # path('categories/', category_list),
    # path('categories/<int:category_id>/', category_detail),

    path('login/', obtain_jwt_token),

    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),

    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),

]
