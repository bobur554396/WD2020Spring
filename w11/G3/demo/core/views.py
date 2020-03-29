from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import Http404

from core.models import Product


def product_list(request):
    # select * from core_product;
    if request.method == 'GET':
        # select * from product where name like %product%;
        # products = Product.objects.filter(name__contains='product')

        # select * from product where name like product%;
        # products = Product.objects.filter(name__startswith='product')

        # select * from product where name like %1;
        # products = Product.objects.filter(name__endswith='1')

        # products = Product.objects.filter(name='product 1')
        # products = Product.objects.filter(name__exact='product 1')

        # products = Product.objects.filter(name__in=['product 1', 'product 3'])

        # products = Product.objects.filter(description__isnull=True)

        # ASC
        # DESC
        products = Product.objects.filter(price__gte=1000).order_by('-price')

        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    elif request.method == 'POST':
        pass


def product_detail(request, product_id):
    # select * from core_product where id=<product_id>;
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.to_json())
