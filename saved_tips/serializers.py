from django.db import IntegrityError
from rest_framework import serializers
from .models import SavedTip


class SavedTipSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SavedTip
        fields = [
            'id', 
            'owner', 
            'created_at',
            'tip'
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'you already saved this tip'
            })