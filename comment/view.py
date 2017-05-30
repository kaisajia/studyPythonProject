from block.models import Block
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from article.models import Article
from .models import Comment
import json

def create_comment(request):
    com = json.loads(request.GET.get("param")
    aid = int(com["article_id"])
    content = com["content"]
    user = com["user"]
    article = Article.objects.get(id=aid)
    print("aid...........",aid,"..........comment.............",comment)
    Comment.article = article
    Comment.owner = user
    Comment.content = content
    Comment.save()
    json_str = json.dumps(ret)
    return HttpResponse(json_str)







