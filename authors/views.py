from django.http import Http404
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from .models import TipAuthor
from tips.models import Tip
from .serializers import TipAuthorSerializer
from DRIVE.permissions import IsOwnerOrReadOnly

# Create your views here.

class TipAuthorList(generics.ListAPIView):
    """
    Lists all authors. 
    No create (auto creation when user created)
    """
    queryset = TipAuthor.objects.annotate(
        number_tips_created = Count('owner__tip', distinct=True),
    ).order_by('-created_on')
    serializer_class = TipAuthorSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'number_tips_created',
        'created_on',
    ]


class TipAuthorDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve details for specific author.
    Users can only edit own details
    """
    serializer_class = TipAuthorSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = TipAuthor.objects.annotate(
        number_tips_created = Count('owner__tip', distinct=True),
    ).order_by('-created_on')