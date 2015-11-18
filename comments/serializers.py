# -*- coding: utf-8 -*-
from comments.models import Comment
from django.template.loader import render_to_string
from rest_framework import serializers

__author__ = 'Pavel Dik'


class CommentHTMLSerializer(serializers.ModelSerializer):
    html = serializers.SerializerMethodField()

    def get_html(self, obj):
        return render_to_string('comments/comment.html', {'comment': obj})

    class Meta:
        model = Comment
        fields = ('html',)


class CommentSerializer(serializers.ModelSerializer):
    def validate(self, data):
        reply_to = data.get('reply_to', None)
        if reply_to:
            if reply_to.page_url != data['page_url']:
                raise serializers.ValidationError("page_url reply_to not equal object page_url ")
        return data

    class Meta:
        model = Comment
        fields = ('text', 'user', 'reply_to', 'page_url')
