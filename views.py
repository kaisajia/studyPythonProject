
from django.shortcuts import render

def index(request):
    #block_infos=[{"name":"运维专区","desc":"运维学习讨论区","manager":"admin"},
    #    {"name":"Django专区","desc":"Django学习讨论区","manager":"admin"},
    #    {"name":"部落建设","desc":"有关部落建设的事宜","manager":"admin"}    
    #]
    
    block_infos=Block.objects.all().order_by("-id")
    return render(request,"index.html",{"blocks":block_infos})