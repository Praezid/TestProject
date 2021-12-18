from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view


def index(request):
    product_count = Product.objects.all().count()
    products = Product.objects.all()
    return render(
        request,
        'index.html',
        context={'product_count': product_count, 'products': products},
    )

def median_value(queryset, term):
    count = queryset.count()
    return queryset.values_list(term, flat=True).order_by(term)[int(round(count/2))]

# API CRUD
@api_view(['POST', 'DELETE'])
def products(request):
    if request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Product.objects.all().delete()
        return JsonResponse({'message': '{} Products were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def products_pk(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The products does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        product_serializer = ProductSerializer(product)
        return JsonResponse(product_serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def count(request):
    if request.method == 'GET':
        count = Product.objects.all().count()
        return JsonResponse({'message': 'The count of products in the storage',
                             'count': f'{count}'})


@api_view(['GET'])
def expensivest(request):
    if request.method == 'GET':
        product = Product.objects.latest('price')
        return JsonResponse({'message': 'The expensivest product in the storage',
                             'product': f'{product}'})



@api_view(['GET'])
def cheapest(request):
    if request.method == 'GET':
        product = Product.objects.latest('-price')
        return JsonResponse({'message': 'The cheapest product in the storage',
                             'product': f'{product}'})


@api_view(['GET'])
def median(request):
    if request.method == 'GET':
        ordered_products = Product.objects.order_by('price')
        return JsonResponse({'message': 'The median product in the storage',
                             'product': f'{ordered_products}'})