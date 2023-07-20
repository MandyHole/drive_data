from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author Model
    Checks if current user is owner
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    number_tips_created = serializers.ReadOnlyField()
    number_tips_saved = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Author
        fields = [
            'id',
            'owner',
            'name',
            'bio',
            'created_on',
            'updated_on',
            'image',
            'is_owner',
            'number_tips_created',
            'number_tips_saved'
        ]
