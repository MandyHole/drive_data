from rest_framework import serializers
from .models import TipAuthor

class TipAuthorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TipAuthor
        fields = [
            'id', 'owner', 'name', 'bio', 'created_on', 'updated_on', 'privacy_preference', 'image'
        ]

