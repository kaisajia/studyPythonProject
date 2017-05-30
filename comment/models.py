from django.db import models
from django.contrib.auth.models import User
from article.models import Article



class Comment(models.Model):
    owner = models.ForeignKey(User,verbose_name="作者")
    article = models.ForeignKey(Article,verbose_name="文章ID") 
    content = models.CharField("内容",max_length=10000)
    status = models.IntegerField("状态",choices=((0,'正常'),(-1,'删除')),default=0)
    create_timestamp = models.DateTimeField("创建时间",auto_now_add=True)
    last_update_timestamp = models.DateTimeField("更新时间",auto_now=True)
    
    
    def __str__(self):
        return self.content
    class Meta:
        verbose_name="评论"
        verbose_name_plural="评论"    
    