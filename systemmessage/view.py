from django.shortcuts import render
from django.shortcuts import redirect
from .models import SystemMessage
from article.models import Article
from comment.models import Comment
from article.paginate import paginate_queryset  

def create_message(owner,content,article,to_comment):
    if to_comment:
        message_content = "有人评价了你的评论'"+content +"'"
        owner = to_comment.owner
    else:
        message_content = "有人评价了你的文章'"+content +"'"
        owner = article.owner 
    link= "/article/"+str(article.block.id)+"/article_detail/"+str(article.id)
    print(message_content,'.......',link) 
    message = SystemMessage(owner=owner,content=message_content,link=link,status=0)
    print('message.............',message)
    message.save() 
  

# def message_cnt(user):
#     print("enter msg_cnt...............")
#     messages = SystemMessage.objects.filter(owner=user,status=0)
#     page_messages,page_data = paginate_queryset(messages,1,cnt_per_age=1)
#     message_count = page_data["count"] 
#     return message_count

def message_list(request):
    user = request.user
    page_no = int(request.GET.get("page_no","1"))
    messages = SystemMessage.objects.filter(owner=user,status=0)
    page_messages,paginate_data = paginate_queryset(messages,page_no,cnt_per_age=7)
      
    return render(request,"message_list.html",{"systemmessages":page_messages,"paginate_data":paginate_data})


def message_read(request):
    user = request.user
    messageId = int(request.GET.get("messageId"))
    sysmessage = SystemMessage.objects.filter(id=messageId)
    message = sysmessage[0]
    message.status=1 
    message.save()
    link = message.link 
    return redirect(link)
    