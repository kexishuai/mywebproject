from django.shortcuts import render,redirect,reverse
from .models import *
# 首页
def home(request):
    # 轮播
    wheels = MainWheel.objects.all()
    navs = MainNav.objects.all()
    mustbuys = MainMustbuy.objects.all()
    shops = MainShop.objects.all()
    shop0 = shops.first()
    shop1_2 = shops[1:3]
    shop3_6 = shops[3:7]
    shop7_10 = shops[7:11]
    mainshows = MainShow.objects.all()
    data ={
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shop0': shop0,
        'shop1_2': shop1_2,
        'shop3_6': shop3_6,
        'shop7_10': shop7_10,
        'mainshows': mainshows,
    }
    return render(request,'home/home.html',data)

# 闪购
def market(request):
    return redirect(reverse('App:market_with_params', args=['104749', '0', '0']))


# 带参数的闪购
def market_with_params(request, typeid, typechildid, sortid):

    # 分类数据
    foodtypes = FoodType.objects.all()
    # 商品数据,根据主分类id进行筛选
    goods_list = Goods.objects.filter(categoryid=typeid)

    # 再按照子分类进行筛选
    if typechildid != '0':
        goods_list = goods_list.filter(childcid=typechildid)

    # 获取当前主分类下的所有子分类
    childnames = FoodType.objects.filter(typeid=typeid)
    # '全部分类:0#进口水果:103534#国产水果:103533'

    child_type_list = []  # 存放子分类的数据
    if childnames.exists():
        childtypes = childnames.first().childtypenames.split('#')
        # print(childtypes)  # ['全部分类:0', '进口水果:103534', '国产水果:103533']

        for type in childtypes:
            type_list = type.split(':')  # ['进口水果', '103534']
            child_type_list.append(type_list)

    # print(child_type_list)
    # [['全部分类', '0'], ['进口水果', '103534'], ['国产水果', '103533']]

    # 排序规则
    if sortid == '0':  # 综合排序
        pass
    elif sortid == '1':  # 销量排序
        goods_list = goods_list.order_by('-productnum')
    elif sortid == '2':  # 价格降序
        goods_list = goods_list.order_by('-price')
    elif sortid == '3':  # 价格升序
        goods_list = goods_list.order_by('price')

    data = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'typeid': typeid,
        'child_type_list': child_type_list,
        'typechildid': typechildid,
    }

    return render(request, 'market/market.html', data)


def cart(request):
    return render(request,'cart/cart.html')

def mine(request):
    return render(request,'mine/mine.html')
