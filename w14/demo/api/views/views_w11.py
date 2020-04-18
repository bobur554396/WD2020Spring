from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Category, Product


@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_json = [c.to_json() for c in categories]
        return JsonResponse(categories_json, safe=False)
    elif request.method == 'POST':
        # create new product
        return JsonResponse({'data': 'product post request'})


@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(category.to_json())


def category_products(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.products.all()
    products_json = [p.to_json() for p in products]

    return JsonResponse(products_json, safe=False)

