from rest_framework import serializers

from goods.models import Goods,GoodsCategory

class CategorySerializer3(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = '__all__'

class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=True,max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.ImageField()
    #
    # def create(self, validated_data):
    #     return Goods.objects.create(**validated_data)
    #
    # 实例化覆盖外键
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'
        #fields = ('name','click_num','market_price','add_time')

