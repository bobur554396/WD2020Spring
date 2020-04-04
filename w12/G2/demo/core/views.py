from django.http.response import JsonResponse

from core.models import Product


def product_list(request):
    # products = Product.objects.all()

    # select * from products where name like %duct%;
    # products = Product.objects.filter(name__contains='duct')

    # select * from products where name like product%;
    # products = Product.objects.filter(name__startswith='product')

    # select * from products where name like %2;
    # products = Product.objects.filter(name__endswith='2')

    # select * from products where name=product 1;
    # products = Product.objects.filter(name='product 1')
    # products = Product.objects.filter(name__exact='product 1')

    # select * from products where price in (1000, 2000);
    # products = Product.objects.filter(price__in=[1000, 2000])

    # products = Product.objects.filter(price__gte=1000)

    # ASC
    # DESC
    products = Product.objects.filter(price__gte=1000).order_by('-name')

    products_json = [product.short() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        # select * from products where id=<product_id>;
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.full())
