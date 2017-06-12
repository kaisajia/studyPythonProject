from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display=("block","title","content","status","create_timestamp","last_update_timestamp")
    actions= ["make_picked"]
    
    def make_picked(self,request,queryset):
        for a in queryset:
            a.status=10
            a.save()
            
    make_picked.short_description="设置精华"
    
admin.site.register(Article)