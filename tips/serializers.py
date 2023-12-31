from rest_framework import serializers
from .models import Tip
from saved_tips.models import SavedTip
from rating.models import Rating


class TipSerializer(serializers.ModelSerializer):
    """
    Serializier for Tip
    Checks for ownership

    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_id = serializers.ReadOnlyField(source='owner.id')
    saved_tips_id = serializers.SerializerMethodField()
    average_rating = serializers.ReadOnlyField()
    number_times_saved = serializers.ReadOnlyField()
    rating_id = serializers.SerializerMethodField()

    def get_saved_tips_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            saved = SavedTip.objects.filter(
                owner=user, tip=obj
            ).first()
            return saved.id if saved else None
        return None

    def get_rating_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                owner=user, tip=obj
            ).first()
            return rating.id if rating else None
        return None

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
            'owner_id',
            'is_owner',
            'title',
            'tip_content',
            'category',
            'ability',
            'screenshot',
            'created_on',
            'updated_on',
            'saved_tips_id',
            'average_rating',
            'number_times_saved',
            'rating_id'
        ]
