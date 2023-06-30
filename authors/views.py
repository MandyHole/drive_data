from django.http import Http404
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from .models import Author
from tips.models import Tip
from .serializers import AuthorSerializer
from drive_api.permissions import IsOwnerOrReadOnly

# Create your views here.

class AuthorList(generics.ListAPIView):
    """
    Lists all authors. 
    No create (auto creation when user created)
    """
    queryset = Author.objects.annotate(
        number_tips_created = Count('owner__tip', distinct=True),
    ).order_by('-created_on')
    serializer_class = AuthorSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'number_tips_created',
        'created_on',
    ]


class AuthorDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve details for specific author.
    Users can only edit own details
    """
    serializer_class = AuthorSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Author.objects.annotate(
        number_tips_created = Count('owner__tip', distinct=True),
    ).order_by('-created_on')