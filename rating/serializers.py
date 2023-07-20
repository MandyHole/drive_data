from django.db import IntegrityError
from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """ 
    Serializer for Rating Model
    Checks for ownership
    Create method checks their is a unique relationship for tip/owner 
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Rating
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'tip_rating',
            'tip',
            'is_owner'

        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'you already rated this tip'
            })
