# -*- coding: utf-8 -*-
from django.contrib import admin

from db.articles.models import PostLike, Post, PostUnlike


class PostLikeInline(admin.TabularInline):
    model = PostLike
    extra = 0


class PostUnlikeInline(admin.TabularInline):
    model = PostUnlike
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('id',)
    inlines = (PostLikeInline, PostUnlikeInline)
