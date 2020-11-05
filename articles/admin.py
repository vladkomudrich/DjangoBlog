from django.contrib import admin
from .models import Article, Comment, Category

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author_name', 'author_email', 'comment_text', 'date', 'article')
    search_fields = ('author_name', 'author_email', 'comment_text')
    save_on_top = True
    save_as = True

admin.site.register(Article)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
