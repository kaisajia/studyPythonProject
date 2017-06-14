from django.contrib import admin
from .models import Comment


class CommentInline(admin.TabularInline):  ##StackedInline     堆叠内联    TabularInline  表格内联
    model = Comment
    can_delete = False


class CommentAdmin(admin.ModelAdmin):
    list_display=("owner","article","content","status","create_timestamp","last_update_timestamp")

admin.site.register(Comment,CommentAdmin)
 