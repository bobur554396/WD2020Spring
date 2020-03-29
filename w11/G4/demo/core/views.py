from django.http.response import JsonResponse

from core.models import Product


def product_list(request):
    # select * from products;
    if request.method == 'GET':
        # select * from products where name like %product%;
        # products = Product.objects.filter(name__contains='product')

        # select * from products where name like product%;
        # products = Product.objects.filter(name__startswith='product')

        # select * from products where name like %1;
        # products = Product.objects.filter(name__endswith='1')

        # products = Product.objects.filter(name='product 1')
        # products = Product.objects.filter(name__exact='product 1')

        # products = Product.objects.filter(name__in=['product 1', 'product 2'])
        # products = Product.objects.filter(price__in=[2000, 3000])

        # products = Product.objects.filter(description__isnull=False)

        # gt => greater than
        # gte => greater than or equal

        # select * from products where price >= 2000;
        # products = Product.objects.filter(price__lte=2000)

        # products = Product.objects.filter(price=2000)

        # ASC
        # DESC
        products = Product.objects.filter(price__gte=1000).order_by('-name')

        products_json = [product.short() for product in products]
        return JsonResponse(products_json, safe=False)
    elif request.method == 'POST':
        # Must create new Product from request body
        pass


def product_detail(request, product_id):
    try:
        # select * from products where id=<product_id>;
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(product.full())
