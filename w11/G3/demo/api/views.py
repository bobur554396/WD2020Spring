from django.http.response import JsonResponse

from api.models import Category


def category_list(request):
    categories = Category.objects.all()
    categories_json = [c.to_json() for c in categories]

    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(category.to_json())


def category_products(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    # select * from product where category_id=<category.id>
    products = category.products.all()
    products_json = [p.to_json() for p in products]

    return JsonResponse(products_json, safe=False)
