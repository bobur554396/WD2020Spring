from django_filters import rest_framework as filters

from api.models import Product


class ProductFilter(filters.FilterSet):
    # Product.objects.filter(name__contains=name)
    name = filters.CharFilter(lookup_expr='contains')

    # Product.objects.filter(price=price)
    price = filters.NumberFilter(lookup_expr='exact')

    # Product.objects.filter(price__gte=min_price)
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')

    # Product.objects.filter(price__lte=max_price)
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('name', 'price', 'min_price', 'max_price',)

