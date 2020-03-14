from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse


def hello(request):
    return HttpResponse('<h1>hello msg</h1>')


# def product_list(request):
#     return HttpResponse('<h1>product list</h1>')
#
#
# def product_detail(request, product_id):
#     return HttpResponse(f'<h1>product id: {product_id}</h1>')


# products = []
# for i in range(1, 5):
#     products.append(
#         {
#             'id': i,
#             'name': f'product {i}',
#             'price': i * 1000
#         }
#     )

products = [
    {
        'id': i,
        'name': f'product {i}',
        'price': i * 1000

    } for i in range(1, 5)
]


def product_list(request):
    return JsonResponse(products, safe=False)


def product_detail(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product)

    return JsonResponse({'error': 'product does not exists'})
