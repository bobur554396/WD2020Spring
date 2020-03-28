from django.http.response import JsonResponse

from api.models import Category


def categories_list(request):
    categories = Category.objects.all()

    categories_json = [category.short() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.short())


def category_products(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    products = category.products.all()
    products_json = [product.full() for product in products]

    return JsonResponse(products_json, safe=False)
