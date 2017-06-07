from django.db import models
from django.contrib.auth.models import User
from article.models import Article


class DeletedCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=-1)
    
class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=0)

class Comment(models.Model):
    objects = models.Manager()  #默认管理员
    normal_objects = CommentManager()  #评论正常的管理员
    deleted_objects = DeletedCommentManager()  #被删除的评论的管理员
    owner = models.ForeignKey(User,verbose_name="作者")
    article = models.ForeignKey(Article,verbose_name="文章ID") 
    content = models.CharField("内容",max_length=10000)
    to_comment = models.ForeignKey("self",null=True,blank=True,verbose_name="回复评论")
    status = models.IntegerField("状态",choices=((0,'正常'),(-1,'删除')),default=0)
    create_timestamp = models.DateTimeField("创建时间",auto_now_add=True)
    last_update_timestamp = models.DateTimeField("更新时间",auto_now=True)
    
    
    def __str__(self):
        return self.content
    class Meta:
        verbose_name="评论"
        verbose_name_plural="评论"    
    