from django.shortcuts import render
from django.shortcuts import redirect

from block.models import Block
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from article.models import Article
from .models import Comment
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

@csrf_exempt
def create_comment(request):
    article_id = request.POST["article_id"]
    content = request.POST["content"]
    user = request.user
    print(article_id,"----------------------------",content,"-----------------",user)
    
    article = Article.objects.get(id=article_id) 
    try: 
        comment = Comment(article=article,owner=user,content=content,status=0)
        comment.save()
        ret = {"status":"ok","msg":""}
    except Exception as e:
        ret = {"status":"error","msg":e}
    json_str = json.dumps(ret) 
    return HttpResponse(json_str,content_type="application/json") 
    #return HttpResponse(json_str)
 