
from django.shortcuts import render
from block.models import Block
def index(request):
    #block_infos=[{"name":"运维专区","desc":"运维学习讨论区","manager":"admin"},
    #    {"name":"Django专区","desc":"Django学习讨论区","manager":"admin"},
    #    {"name":"部落建设","desc":"有关部落建设的事宜","manager":"admin"}    
    #]
    
    #block_infos=Block.objects.all().order_by("-id")   #all() 取所有数据
    block_infos=Block.objects.filter(status=0).order_by("-id")
    ##取满足filter数据  还可以用不等于条件  __gt=0 是指大于0 status__gte=0 是指大于等于0  __lt=0是指小于0 __lte=0是指小于等于0
    return render(request,"index.html",{"blocks":block_infos})