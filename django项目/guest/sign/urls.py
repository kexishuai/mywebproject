from .views import *
from django.conf.urls import url

urlpatterns = [

    url(r'^index/$',index,name='index'),
    # url(r'^loginaction/$', login_action, name='login_action'),
    url(r'^event/$', event, name='event'),
    url(r'^event_manage/(\d+)/$', event_manage, name='event_manage'),
    url(r'^guest/$', guest, name='guest'),
    url(r'^guest_manage/(\d+)/$', guest_manage, name='guest_manage'),

    url(r'^sreach_name/$', sreach_name, name='sreach_name'),

    #url(r'^login/$', login, name='login'),
    url(r'^loginhandle/$', login_handle, name='login_handle'),
    url(r'^register/$', register, name='register'),
    url(r'^registerhandle/$', register_handle, name='register_handle'),
    url(r'^logout/$', log_out, name='log_out'),

    #签到sign_action
    url(r'^signindex/(\d+)/$', sign_index, name='sign_index'),
    url(r'^signaction/(\d+)/$', sign_action, name='sign_action'),

    #轮播
    url(r'^loop/(\d+)$', loop, name='loop'),

]