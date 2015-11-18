from comments.models import Comment
from django.contrib import admin


# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'reply_to', 'user', 'text', 'deleted')
    list_editable = ('deleted',)
    list_filter = ('page_url', 'user', 'deleted')
    inlines = [CommentInline, ]
