
from django.shortcuts import render 

def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_objs = Article.objects.fileter(block=block,status=0).order_by("-id")
    ##上边看起来像是判断对象相等，其实是django包装了，底层是判断id比对
    ##所以，也可以写成filter(block__id=block_id)
    ## fileter(block=block,status=0)  表示 where block=? and status=?
    ## 如果想表达或，需要使用Q对象,每个Q表示一个条件，用|表示或，from django.db.models import Q 
    ## filter(Q(block=block)|Q(status=0)|Q(x=y)) 
    
    return render(request,"article_list.html",{"articles":article_objs,"b":block})



