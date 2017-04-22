from block.models import Block
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleForm

from django.views.generic import View
from django.views.generic import DeleteView

def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id) 
    article_objs = Article.objects.filter(block=block,status=0).order_by("-id")
    ##上边看起来像是判断对象相等，其实是django包装了，底层是判断id比对
    ##所以，也可以写成filter(block__id=block_id)
    ## fileter(block=block,status=0)  表示 where block=? and status=?
    ## 如果想表达或，需要使用Q对象,每个Q表示一个条件，用|表示或，from django.db.models import Q 
    ## filter(Q(block=block)|Q(status=0)|Q(x=y)) 
    
    return render(request,"article_list.html",{"articles":article_objs,"b":block})

#基于函数实现的处理逻辑：简单快速、但是长期看面临迁移到类  
def publish_article(request,b_id): 
    b_id = int(b_id)
    block = Block.objects.get(id=b_id)
    print(request.method)
    if request.method=="GET":
        return render(request,"publish_article.html",{"bol":block})
    else:
        #第一种判断语句写法
        #title = request.POST["title"].strip()
        #content = request.POST["content"].strip()
        #if not title or not content:
        #    return render(request,"publish_article.html",{"bol":block,"error":"标题或内容不能为空","title":title,"content":content})
        #if len(title)>100 or len(content)>10000:
        #    return render(request,"publish_article.html",{"bol":block,"error":"标题或内容过长","title":title,"content":content})
        #else:
        #    article = Article(block=block,title=form.cleaned_data["title"],content=form.cleaned_data["content"],status=0)
        #    article.save()
        
        #第二种写法：把判断语句 抽出来到forms.py 里
        #form = ArticleForm(request.POST)
        #if form.is_valid():
        #    article = Article(block=block,title=form.cleaned_data["title"],content=form.cleaned_data["content"],status=0)
        #    article.save()
        #    return redirect("/article/list/%s" % b_id)
        #else:
        #    print(form.errors)
        #    return render(request,"publish_article.html",{"bol":block,"form":form})
         
        #第三种写法：整合,先用form.save提交form中的信息，保存在内存中
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = block
            article.status=0
            article.save()
            return redirect("/article/list/%s" % b_id)
        else:
            return render(request,"publish_article.html",{"bol":block,"form":form})
        
#基于类实现处理逻辑，相对复杂，可以使用高级的设计模式       
class ArticleCreate(View):
    template_name="publish_article.html"
    
    def init_data(self,block_id):
        self.block_id = block_id
        self.block = Block.objects.get(id=block_id)
        
    def get(self,request,block_id):
        self.init_data(block_id)
        return render(request,self.template_name,{"bol":self.block})
    
    def post(self,request,block_id):
        self.init_data(block_id)
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = self.block
            article.status=0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request,"publish_article.html",{"bol":self.block,"form":form})




#####文章详情页面也使用两种方式分别实现一下
###基于函数

def article_detail(request,block_id,aid):
    block_id = int(block_id)
    aid = int(aid)
    block = Block.objects.get(id=block_id) 
    article = Article.objects.get(id=aid)
    print(block_id,block.name,block.manager_name)
    return render(request,"article_detail.html",{"block_id":block_id,"block_name":block.name,"art":article})


###基于类









