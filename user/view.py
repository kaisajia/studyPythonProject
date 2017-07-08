from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
import sys,re

#from .forms import UserForm



def register(request):
    if request.method=="GET":
        print("request.method............:",request.method)
        return render(request,"register.html")     
    
    #else:
    #    form = UserForm(request.POST)
    #    print("request.method............:",request.method,"...,form............................:",form)
    #   if form.is_valid():
    #        user = form.save()
    #       return redirect("register_success.html")
    #    else:
    #        return render(request,"register.html",{"form":form})
        
    else:
        username = request.POST["username"].strip()
        email = request.POST["email"].strip()
        password = request.POST["password"].strip()
        user_password_agin = request.POST["user_password_agin"].strip()
        
         ##验证输入内容不能为空
        if not (username and email and password and user_password_agin): 
            return render(request,"register.html",{"username":username,"email":email,"password":password,"error":"用户名，邮箱，密码均不能为空"})
        
        ## 验证密码是否够安全
        if len(password)<6 or re.match(r'^(?=.*[A-Za-z])(?=.*[0-9])\w{6,}$',password):   ##字符与数据混合使用逻辑还没写
            return render(request,"register.html",{"username":username,"email":email,"password":password,"error":"密码强度不够,密码最少6位字符+数据"})
        
        #对比再次密码是否一致
        if password!=user_password_agin:  
            return render(request,"register.html",{"username":username,"email":email,"password":password,"error":"确认密码不正确"})
        
        ##验证用户名否已经存在
        all_users = User.objects.all()
        for user in all_users:
            if username==user.username:
                return render(request,"register.html",{"username":username,"email":email,"password":password,"error":"用户名已存在"})
            
        ###验证邮箱是否符合邮箱格式
         
        
        else: 
            user = User(username=username,email=email,password=password)
            user.save()
            return redirect("/accounts/login")


def register_success(request): 
    return render(request,"register_success.html")

def user_logout(request): 
    return render(request,"registration/user_logout.html")

 
def change_passwd(request): 
    return render(request,"registration/password_change_form.html")












