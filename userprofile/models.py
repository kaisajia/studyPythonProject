from django.db import models
from django.contrib.auth.models import User

class UserPofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    sex = models.IntegerField("性别",choices=((1,"男"),(2,"女")),default=0)
    birthday = models.DateTimeField("生日",null=True,blank=True)
    
 
    class Meta:
        verbose_name="个人档案"
        verbose_name_plural="个人档案"
        
        
        
        
        
        
        