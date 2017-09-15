from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from api.serializers import ProductSerializer
from api.models import Product


# Create your views here.

class GetMessageView(APIView):
 	# get 请求
    def get(self, request):
    	# 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('a')
        print(a)
        # 返回信息
        d = {
            'status': 1,
            'message': 'success',
            }
        return JsonResponse(d)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @detail_route()
    def changeName(self, request, *args, **kwargs):
        get = request.GET
        product = self.get_object()
        product.name = get.get('newName')
        product.save()

        return Response(product.name)

    @list_route()
    def filterProducts(self, request):
        products = Product.objects.filter(id__in=range(3))
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

