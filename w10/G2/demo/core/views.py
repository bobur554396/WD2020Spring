from django.http.response import JsonResponse
from django.http import Http404

from core.models import Product


def product_list(request):
    # select * from products;
    products = Product.objects.all()
    products_json = [product.short() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        # select * from products where id=<product_id>;
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.full())
