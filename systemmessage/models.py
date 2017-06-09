from django.db import models
from django.contrib.auth.models import User


class SystemMessage(models.Model): 
    owner = models.ForeignKey(User,verbose_name="作者")
    content = models.CharField("内容",max_length=10000)
    link = models.CharField("事件发生链接",max_length=10000)
    status = models.IntegerField("状态",choices=((1,'已读'),(0,'未读')),default=0)
    create_timestamp = models.DateTimeField("创建时间",auto_now_add=True)
    last_update_timestamp = models.DateTimeField("更新时间",auto_now=True)
    
    
    def __str__(self):
        return self.content
    class Meta:
        verbose_name="系统消息"
        verbose_name_plural="系统消息"
        
        
        
        