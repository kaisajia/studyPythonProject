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
from systemmessage.view import create_message

@csrf_exempt
def create_comment(request):
    article_id = request.POST["article_id"]
    content = request.POST["content"]
    user = request.user
    to_comment_id = int(request.POST.get("to_comment_id",0))  
    if to_comment_id !=0:
        to_comment = Comment.objects.get(id=to_comment_id,status=0)
    else:
        to_comment = None
    print(request,"...........",article_id,"----------------------------",content,"-----------------",user,"-----------",to_comment_id)
     
    article = Article.objects.get(id=article_id) 
    try: 
        comment = Comment(article=article,owner=user,content=content,status=0,to_comment=to_comment)
        comment.save()
        #create_message(owner=user,content=content,status=0,to_comment=to_comment)
        ret = {"status":"ok","msg":""}
    except Exception as e:
        ret = {"status":"error","msg":e}
    json_str = json.dumps(ret) 
    return HttpResponse(json_str,content_type="application/json") 
    #return HttpResponse(json_str)
 