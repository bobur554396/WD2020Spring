from rest_framework import generics
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from api.filters import ProductFilter
from api.models import Category, Product

from api.serializers import CategorySerializer2, ProductSerializer, \
    CategoryWithProductsSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2
    # permission_classes = (IsAuthenticated,)


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer2


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)
    # pagination_class = PageNumberPagination
    # pagination_class = LimitOffsetPagination

    # uses DjangoFilterBackend
    # filterset_fields = ('name', 'price',)
    filter_class = ProductFilter

    # uses SearchFilter
    search_fields = ('name', 'price',)

    # uses OrderingFilter
    ordering_fields = ('name', 'price')




class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
