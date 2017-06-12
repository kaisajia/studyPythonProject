from block.models import Block
from systemmessage.view import message_cnt

from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleForm

from comment.models import Comment
from django.views.generic import View
from django.views.generic import DeleteView
from django.views.generic import DetailView

from .paginate import paginate_queryset
 

def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    page_no = int(request.GET.get("page_no","1"))
    all_articles = Article.objects.filter(block=block,status=0).order_by("-id")
 
    ###页面上需要分布的变量 
    page_articles,paginate_data = paginate_queryset(all_articles,page_no)
    
    return render(request,"article_list.html",{"articles":page_articles,"b":block,"paginate_data":paginate_data})



ARTICLE_CNT_1PAGE = 3     ##定义每页显示多少
def article_list_v1(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    #article_objs = Article.objects.filter(block=block,status=0).order_by("-id") 
    ##实现分布 需要的变更  
    page_no = int(request.GET.get("page_no","1"))   ##当前页码 ，如果没有相应参数，默认给出1 
    start_index = (page_no-1) * ARTICLE_CNT_1PAGE   ##当前页数据的起始索引
    end_index = page_no * ARTICLE_CNT_1PAGE         ##当前页数据的结束索引
    
    all_articles = Article.objects.filter(block=block,status=0).order_by("-id")
    p = Paginator(all_articles,ARTICLE_CNT_1PAGE)
    page = p.page(page_no)
    articles = page.object_list
    
    ###页面上需要分布的变量 
    page_nums = p.num_pages  #总页数 
    page_links = [i for i in range(page_no-3,page_no+4) if i>0 and i<=page_nums]  ##标页列表
    page_first = page_links[0]-1   ###标页列表最小页
    page_max = page_links[-1]-1    ###标页列表最大页
    print("page_nums.type:",type(page_nums))
    #page_next = page_max <= page_nums    ###是否有后一页
    #page_pre = page_first > 0 ###是否有前一页
        
    
    ##上边看起来像是判断对象相等，其实是django包装了，底层是判断id比对
    ##所以，也可以写成filter(block__id=block_id)
    ## fileter(block=block,status=0)  表示 where block=? and status=?
    ## 如果想表达或，需要使用Q对象,每个Q表示一个条件，用|表示或，from django.db.models import Q 
    ## filter(Q(block=block)|Q(status=0)|Q(x=y)) 
    
    return render(request,"article_list.html",{"articles":articles,"b":block,"page_nums":page_nums,"page_links":page_links,"page_first":page_first,"page_max":page_max,"page_no":page_no,"page_next":page_no+1,"page_pre":page_no-1})

#基于函数实现的处理逻辑：简单快速、但是长期看面临迁移到类

def publish_article(request,b_id): 
    b_id = int(b_id)
    block = Block.objects.get(id=b_id) 
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
        #self.owner = User.objects.get(id)
        
    def get(self,request,block_id):
        print("request.method............:",request.method)
        self.init_data(block_id)
        return render(request,self.template_name,{"bol":self.block})
    
    def post(self,request,block_id): 
        self.init_data(block_id) 
        self.user = request.user
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = self.block
            article.owner = self.user
            article.status=0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request,"publish_article.html",{"bol":self.block,"form":form})




#####文章详情页面也使用两种方式分别实现一下
###基于函数
 
###2017-05-30 增加评论展示

def article_detail(request,block_id,aid):
    block_id = int(block_id)
    aid = int(aid)
    block = Block.objects.get(id=block_id) 
    article = Article.objects.get(id=aid)
        
    ##评论内容及评论分页
    #all_comments = Comment.objects.filter(article = aid,status=0).order_by("-create_timestamp")  ###order_by ("-column_name")  表示降序
    all_comments = Comment.normal_objects.filter(article=aid).order_by("-create_timestamp")  ##增加数据管理员逻辑
    page_no = int(request.GET.get("page_no","1"))
    page_comments,paginate_data = paginate_queryset(all_comments,page_no)
    #print("all_comments..........",all_comments.size)
    msg_cnt = message_cnt(request.user)
    print(block_id,block.name,block.manager_name,msg_cnt)
    return render(request,"article_detail.html",{"block_id":block_id,"block_name":block.name,"art":article,"comments":page_comments,"paginate_data":paginate_data,"msg_cnt":msg_cnt})


###基于类

class ArticleDetailView(DetailView):
    model = Article
    tempate_name = 'article_detail.html'
    context_object_name = 'article'

    def init_data(self,block_id,aid):
        self.block_id = block_id
        self.block = Block.objects.get(id=block_id)
        self.aid = aid
        self.article = Article.objects.get(id = aid)
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_no = int(self.request.GET.get("page_no","1"))
        all_comments = Comment.objects.filter(article=context["article"],status=0)
        print("all_comments...............",all_comments)
        comments,pagination_data = paginate_queryset(all_comments,page_no,cnt_per_page=3)
        context['comments'] = comments
        
        return context

    def get(self,request,block_id,aid):
        print("request.method............:",request.method)
        self.init_data(block_id,aid)
        return render(request,self.template_name,{"block_id":block_id,"block_name":block.name,"art":article})
    
    def post(self,request,block_id): 
        self.init_data(block_id,aid)
        self.user = request.user
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = self.block
            article.owner = self.user
            article.status=0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request,"article_detail.html",{"bol":self.block,"form":form})







