import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Category


# CRUD - For Category Model

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_json = [c.to_json() for c in categories]
        return JsonResponse(categories_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)

        # option 1
        # category = Category(name=data['name'])
        # category.save()

        # option 2
        category = Category.objects.create(name=data.get('name'))

        return JsonResponse(category.to_json())


@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    # Get one objects
    if request.method == 'GET':
        return JsonResponse(category.to_json())

    # Update selected objects
    elif request.method == 'PUT':
        data = json.loads(request.body)

        category.name = data.get('name', category.name)
        category.save()

        return JsonResponse(category.to_json())

    # Delete selected object
    elif request.method == 'DELETE':
        category.delete()

        return JsonResponse({'deleted': True})
