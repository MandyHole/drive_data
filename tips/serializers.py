from rest_framework import serializers
from .models import Tip

class TipSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    owner_image = serializers.ReadOnlyField(source='owner.tipauthor.image.url')

    def validate_screenshot(self, value):
        if value.size > 1024 * 1024:
            raise serializers.ValidationError(
                "Image size is greater than 1 MB"
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Tip
        fields = [
            'id', 
            'owner', 
            'title', 
            'tip_content', 
            'created_on', 
            'updated_on', 
            'screenshot', 
            'category', 
            'is_owner', 
            'ability',
            'owner_image',
            'owner_id',
        ]
