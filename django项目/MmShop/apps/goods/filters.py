# -*- coding: utf-8 -*-
__author__ = 'bobby'

import django_filters
from django.db.models import Q

from goods.models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(name='shop_price', help_text="最低价格",lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name='shop_price', help_text="最高价格",lookup_expr='lte')
    #name = django_filters.CharFilter(name='name') # 模糊查询

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']