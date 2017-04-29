from django import forms
from .models import Article

#第一种写法
#class ArticleForm(forms.Form):
#    title = forms.CharField(label="标题",max_length=100)
#   content = forms.CharField(label="内容",max_length=10000)
    ## 默认都是必须字段（不能为空），不必须字段可增加参数设置 requried = Flase

#第二种写法，在数据模型中字段量大的时候，比较好用
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ['title','content']

       