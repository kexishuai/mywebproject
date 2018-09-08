"""MmShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MmShop.settings")# project_name 项目名称
django.setup()

from django.conf.urls import url,include
from django.contrib import admin
#from goods.views_base import GoodsListView
from goods.views import GoodsListViewSet,CategoryViewSet


from MmShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter


goods_list = GoodsListViewSet.as_view({
    'get':'list',
})

# 配置ｇｏｏｄｓ的url
router = DefaultRouter()
router.register(r'goods',GoodsListViewSet,base_name='goods')

# 配置categorys的url

router.register(r'categorys',CategoryViewSet,base_name='categorys')

from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    #url(r'goods/$',goods_list,name='goods_list'),
    url(r'^',include(router.urls)),
    url(r'docs/',include_docs_urls(title='暮雪生鲜')),
]
