from django.contrib import admin
from main.models import Article, Author, Comment, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body',)
    search_fields = ('author',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'article', 'created_at',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'birth_date',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
