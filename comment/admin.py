from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display=("owner","article","content","status","create_timestamp","last_update_timestamp")

admin.site.register(Comment)
 