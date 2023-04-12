# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext_lazy as _

from db.base.models import DateTimeModelMixin


class Post(DateTimeModelMixin):
    title = models.CharField(_('title'), max_length=255)
    creator = models.ForeignKey(
        'users.User',
        verbose_name=_('creator'),
        related_name='posts',
        on_delete=models.CASCADE,
    )
    users_liked = models.ManyToManyField(
        'users.User',
        verbose_name=_('likes'),
        related_name='post_liked',
        through='articles.PostLike'
    )
    users_unliked = models.ManyToManyField(
        'users.User',
        verbose_name=_('unlikes'),
        related_name='post_unliked',
        through='articles.PostUnlike'
    )

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class PostLike(DateTimeModelMixin):
    post = models.ForeignKey(
        'articles.Post',
        verbose_name=_('post'),
        related_name='likes',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'users.User',
        verbose_name=_('user'),
        related_name='likes',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('PostLike')
        verbose_name_plural = _('PostLikes')


class PostUnlike(DateTimeModelMixin):
    post = models.ForeignKey(
        'articles.Post',
        verbose_name=_('post'),
        related_name='unlikes',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'users.User',
        verbose_name=_('user'),
        related_name='unlikes',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('PostUnlike')
        verbose_name_plural = _('PostUnlikes')
