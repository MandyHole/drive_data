from rest_framework import serializers
from .models import TipAuthor

class TipAuthorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TipAuthor
        fields = [
            'id', 'owner', 'name', 'bio', 'email', 'created_on', 'updated_on', 'privacy_preference', 'image', 'is_owner'
        ]

