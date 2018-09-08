from django.db import models

# Create your models here.

# 发布会表

class Event(models.Model):
    name = models.CharField(max_length=100)  # 发布会标题
    limit = models.IntegerField() # 参加人数
    status = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField('event time')
    create_time = models.DateTimeField(auto_now=True) # 创建时间，自动获取当前时间

    def __str__(self):
        return self.name
# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event) # 关联发布会id
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField() # 签到状态
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event','phone')  # 发布会id 和手机号作为联合主键

    def __str__(self):
        return self.realname

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    sex = models.BooleanField(default=True)
    icon = models.FileField(max_length=100,null=True,blank=True)
    is_delete = models.BooleanField(default=False)


