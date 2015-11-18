# -*- coding: utf-8 -*-
from comments.models import Comment
from django.db.models import Count

__author__ = 'Pavel Dik'
from django import template

register = template.Library()


@register.inclusion_tag('comments/comments_block.html', takes_context=True)
def comments_block(context):
    return {
        'comments': Comment.objects.annotate(childrens=Count('comment'))
            .filter(page_url=context.request.path, reply_to__isnull=True),
        'page_url': context.request.path
    }
