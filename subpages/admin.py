from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display=['comment','status','created_at']
    list_filter=['status']
    readonly_fields=('comment','smartphone','user','rate','created_at')

admin.site.register(Comment,CommentAdmin)
