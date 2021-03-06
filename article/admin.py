from django.contrib import admin
from .models import Article
from comment.admin import CommentInline
 
class ArticleAdmin(admin.ModelAdmin):
    list_display=("block","title","content","status","create_timestamp","last_update_timestamp")
    fieldsets = (
        ("基本",{"classes":('wide',),"fields":("block","title","content")}),
        ("高级",{"classes":('collapse',),"fields":("status","create_timestamp")})
    )
    readonly_fields=("title","create_timestamp")
    actions= ["make_picked"]
    inlines = [CommentInline]
    def make_picked(self,request,queryset):
        for a in queryset:
            a.status=10
            a.save()
            
    make_picked.short_description="设置精华 "
    
admin.site.register(Article,ArticleAdmin)