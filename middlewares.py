
from django.shortcuts import redirect
from django.shortcuts import render
from systemmessage.models import SystemMessage 
from article.paginate import paginate_queryset  

class GetSysMsgCntMilleware(object):
    
    def __init__(self,get_response):
        self.get_response = get_response
        
        
    def __call__(self,request):
        #控制器代码执行前执行的代码
        isAuthenticated = request.user.is_authenticated()
        if isAuthenticated:
            print("enter msg_cnt...............")
            user = request.user
            messages = SystemMessage.objects.filter(owner=user,status=0)
            page_messages,page_data = paginate_queryset(messages,1,cnt_per_age=1)
            message_count = page_data["count"]
            request.user.msg_cnt = message_count 
            response = self.get_response(request)     ###这句是固定的
      
            #控制器代码执行后执行的代码
            return response  
        else:
            response = self.get_response(request)     ###这句是固定的
            return response  
            
class LogExceptionMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        try:
            response = self.get_response(request)
        except Exception as e:
            LOGGER.exception(e)
            return HttpResponse("报错了！！！")
        return response
    
    
class LoginMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        isAuthenticated = request.user.is_authenticated()
        isLoginReq = "/accounts/login" in request.path
        print("判断是否需要登录。。。。是否认证：",isAuthenticated,"...是否是登录接口:",isLoginReq)
        if isAuthenticated or isLoginReq:
            print('LoginMiddleware........continue')
            response = self.get_response(request) 
            return response 
        else:
            print('LoginMiddleware.........login')
            return redirect("/accounts/login")
    
class PrintParamsMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        print("GET请求参数：",request.GET)
        print("POST请求参数：",request.POST)
        
        response = self.get_response(request)     ###这句是固定的

        #控制器代码执行后执行的代码
        return response 

