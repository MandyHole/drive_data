from rest_framework import serializers
from .models import Tip

class TipSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    author_id = serializers.ReadOnlyField(source='owner.author.id')
    profile_image = serializers.ReadOnlyField(source='owner.author.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Tip
        fields = [
            'id', 
            'author', 
            'title', 
            'tip_content', 
            'created_on', 
            'updated_on', 
            'screenshot', 
            'category', 
            'is_owner', 
            'ability'
        ]
