from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .serializers import GoodsSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import GoodsFilter

from rest_framework import mixins
from rest_framework import generics

from rest_framework import viewsets
from .models import Goods,GoodsCategory

'''
class GoodsListView(APIView):
    def get(self,request,format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods,many=True)
        return Response(goods_serializer.data)

    def post(self,request,format=None):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    '''
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100



class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filter_fields = ('name','shop_price','goods_brief')  # 过滤
    #filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')

class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):

    '''
    商品分类列表数据
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer