from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    author_id = serializers.ReadOnlyField(source='author.id')
    author_image = serializers.ReadOnlyField(source='author.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'author_id', 'author_image'
        )
