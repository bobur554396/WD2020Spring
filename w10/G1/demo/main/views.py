from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse

msg = '<h1>{}</h1>'


def hello(request):
    return HttpResponse('<h1>hello msg</h1>')


# def product_list(request):
#     return HttpResponse(msg.format('products list'))
#
#
# def product_detail(request, product_id):
#     return HttpResponse(msg.format(product_id))

products = [
    {
        'id': i,
        'name': 'product {}'.format(i),
        'price': i * 1000
    }
    for i in range(1, 5)
]


def product_list(request):
    # products = []
    # for i in range(1, 5):
    #     products.append(
    #         {
    #             'name': 'product {}'.format(i),
    #             'price': i * 1000
    #         }
    #     )
    return JsonResponse(products, safe=False)


def product_detail(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product)

    return JsonResponse({'error': 'not found'})
