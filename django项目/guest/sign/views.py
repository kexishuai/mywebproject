import hashlib
import uuid
import os
from guest.settings import MEDIA_ROOT
from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# 登录
#from django.contrib import auth
#from django.contrib.auth.decorators import login_required

from sign.models import Event,Guest,User

# 分页
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

# 首页
def index(request):
    # return HttpResponse('Hello django!')
    return render(request,'index.html')

def guest(request):
    return redirect(reverse('sign:guest_manage',args=[1]))

def event(request):
    return redirect(reverse('sign:event_manage',args=[1]))

# 限制必须登录才能访问
# @login_required
def event_manage(request,num):
    # username = request.COOKIES.get('user','') # 读取浏览器cookie
    event_list = Event.objects.all()
    userid = request.session.get('userid','') # 读浏览器session
    users = User.objects.filter(id=userid)
    p1 = Paginator(event_list, 3)
    page = p1.page(num)
    if users.exists():
        username = users.first().username
        icon = users.first().icon
        data = {
            'userid': userid,
            #'events': event_list,
            'username':username,
            'icon':'/upload/icon/' + str(icon),
            'page': page,
            'page_range': p1.page_range
        }

    return render(request,'event_manage.html',data)

def guest_manage(request,num):
    # username = request.COOKIES.get('user','') # 读取浏览器cookie
    guest_list = Guest.objects.all()
    userid = request.session.get('userid','') # 读浏览器session
    users = User.objects.filter(id=userid)
    icon = users.first().icon
    username = users.first().username
    p= Paginator(guest_list,3)
    page = p.page(num)
    data = {
        'userid': userid,
       # 'guests': guest_list,
        'icon': '/upload/icon/' + str(icon),
        'username':username,
        'page':page,
        'page_range':p.page_range
    }
    return render(request,'guest_manage.html',data)

# 发布会名称搜索
def sreach_name(request):
    userid = request.session.get('userid','')
    users = User.objects.filter(id=userid)
    sreach_name = request.GET.get('name','')
   # sreach_name_bytes = sreach_name.encode(encoding='utf-8')
    event_list = Event.objects.filter(name__contains=sreach_name)
    guest_list = Guest.objects.filter(realname__contains=sreach_name)
    if users.exists():
        username = users.first().username
        icon = users.first().icon
    if event_list or guest_list:
        data = {
            'userid': userid,
            'username':username,
            'icon': '/upload/icon/' + str(icon),
            'event_list': event_list,
            'guest_list':guest_list,
        }
        return render(request, 'sreach.html', data)
    else:
        data = {
            'userid': userid,
            'msg':'您搜索的内容不存在！',
        }
        return render(request, 'sreach.html', data)
# 注册
def register(request):
    return render(request,'user/register.html')

def register_handle(request):
    data = {
        'status':1,
        'msg':'OK',
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon','')

        if len(username) < 6:
            data['status'] = 0
            data['msg'] = '用户名不合法!'
            return render(request, 'user/register.html')
        try:
            user = User()
            user.username=username
            user.password=password
            user.email= email

            if icon:

                filename = random_file() + '.png'   # icon.name
                user.icon = filename

                filepath = os.path.join(MEDIA_ROOT, filename)
                with open(filepath, 'ab') as fp:
                    for part in icon.chunks():
                        fp.write(part)
                        fp.flush()
            else:
                user.icon = ""

            user.save()

            request.session['userid'] = user.id
            return redirect(reverse('sign:index'))

        except:
            render(request, 'user/register.html')

    return render(request,'user/register.html')

def random_file():
    u = str(uuid.uuid4())
    m = hashlib.md5()
    m.update(u.encode('utf-8'))
    return m.hexdigest()

# 登录
def login(request):
    return render(request,'index.html')

def login_handle(request):
    data = {
        'status':1,
        'msg':'ok',
    }
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(username=username,password=password)
        if users.exists():
           request.session['userid'] = users.first().id

           return redirect(reverse('sign:event'))
        else:
            data['status'] = 0
            data['msg'] = '用户名或密码错误!'
            return render(request, 'index.html',data)
    else:
        data['status'] = -1
        data['msg'] = '请求方式错误'
        return render(request, 'index.html',data)
    return render(request, 'index.html')
#退出登录
def log_out(request):
    # 退出删除ｓｅｓｓｉｏｎ
    request.session.flush()
    return redirect(reverse('sign:index'))

# 签到
def sign_index(request,event_id):
    userid = request.session.get('userid','')

    users = User.objects.filter(id=userid)
    events = Event.objects.filter(id=event_id)
    eventname = events.first().name
    eventid = events.first().id
    if users:
        username = users.first().username
        icon = users.first().icon
    data = {
        'eventname':eventname,
        'eventid':eventid,
        'username':username,
        'icon':'/upload/icon/'+str(icon)
    }
    return render(request,'sign_index.html',data)

def sign_action(request,event_id):
    data = {
        'status':1,
        'msg':'ok',
    }
    if request.method == 'POST':
        phone = request.POST.get('phone')
        userid = request.session.get('userid','')
        users = User.objects.filter(id=userid)
        event = Event.objects.get(id=event_id)
        guest = Guest.objects.filter(phone=phone).first()

        if not guest:
            data['status'] = 0
            data['msg'] = '您输入的手机号为空或有误，请重新输入！'
            data['eventname'] = event.name
            data['eventid'] = event.id
            data['username'] = users.first().username
            data['icon'] = '/upload/icon/'+str(users.first().icon)
            return render(request, 'sign_index.html', data)
        result = Guest.objects.filter(event_id=event.id,phone=phone)
        if not result:
            data['msg'] = '您还未参加任何发布会！'
            data['status'] = 0
            data['eventname'] = event.name
            data['eventid'] = event.id
            data['username'] = users.first().username
            data['icon'] = '/upload/icon/' + str(users.first().icon)
            return render(request, 'sign_index.html', data)

        if result.first().sign:
            data['msg'] = '您已签到！'
            data['status'] = 0
            data['eventname'] = event.name
            data['eventid'] = event.id
            data['username'] = users.first().username
            data['icon'] = '/upload/icon/' + str(users.first().icon)
            return render(request, 'sign_index.html', data)
        else:

            Guest.objects.filter(phone=phone).update(sign='1')
            # data['eventname'] = event.name
            # data['eventid'] = event.id
            # data['username'] = users.first().username
            # data['icon'] = '/upload/icon/' + str(users.first().icon)
            # return render(request,'loop.html',data)
            #使用重定向，ｐｏｓｔ请求在浏览器不会显示重新提交表单
            return redirect(reverse('sign:loop',args=[event_id]))
    else:
        data['status'] = -1
        data['msg'] = '请求方式错误!'
        return JsonResponse(data)

def loop(request,event_id):
    data = {
        'status':1,
        'msg':'ok',
    }
    userid = request.session.get('userid', '')
    users = User.objects.filter(id=userid)
    event = Event.objects.get(id=event_id)
    data['eventname'] = event.name
    data['eventid'] = event.id
    data['username'] = users.first().username
    data['icon'] = '/upload/icon/' + str(users.first().icon)
    return render(request,'loop.html',data)





