from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    owner_image = serializers.ReadOnlyField(source='owner.tipauthor.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'owner_image',
            'owner_id',
            'created_at',
            'updated_at',
            'content',
            'tip'
        ]


class CommentDetailSerializer(CommentSerializer):
    tip = serializers.ReadOnlyField(source='tip.id')
