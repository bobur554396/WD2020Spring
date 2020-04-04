from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.models import Product


@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        # select * from product where name like %product%;
        # products = Product.objects.filter(name__contains='chan')

        # select * from product where name like prod%;
        # products = Product.objects.filter(name__startswith='prod')

        # products = Product.objects.filter(name='product 1')
        # products = Product.objects.filter(name__in=['product 1', 'product 3'])

        products = Product.objects.filter(price__gte=1000).order_by('name')
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    elif request.method == 'POST':
        # create new product
        return JsonResponse({'data': 'product post request'})


@csrf_exempt
def product_detail(request, product_id):
    try:
        # select * from product where id=product_id;
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(product.to_json())
    elif request.method == 'PUT':
        # update product object
        pass
    elif request.method == 'DELETE':
        # delete selected object
        pass
