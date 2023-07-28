from django.http import Http404
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tip
from .serializers import TipSerializer
from drive_api.permissions import IsOwnerOrReadOnly
from rating.models import Rating
from django.db.models import Avg, Count
from saved_tips.models import SavedTip
from django.db.models import F


# Create your views here.

class CustomOrderingFilter(filters.OrderingFilter):
    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)

        def make_f_object(x):
            return F(x[1:]).desc(
                nulls_last=True) if x[0] == '-' else F(x).asc(
                    nulls_last=True)

        if ordering:
            ordering = map(make_f_object, ordering)
            queryset = queryset.order_by(*ordering)

        return queryset


class TipList(generics.ListCreateAPIView):
    """
    List all tips
    Can create a new tip if logged in
    """
    queryset = Tip.objects.annotate(
        average_rating=Avg('rating__tip_rating'),
        number_times_saved=Count('author_saved_tip', distinct=True),
    ).order_by('-created_on')
    filter_backends = [
        CustomOrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
        ]
    search_fields = [
        'title',
        'tip_content',
        'ability',
        'category'
    ]
    filterset_fields = [
        'owner__author',
        'author_saved_tip__owner__author',
        'category',
        'ability'
        ]
    ordering_fields = [
        'average_rating',
        'owner',
        'ability',
        'category',
        'number_times_saved'
    ]
    serializer_class = TipSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TipDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves a specific tip
    Only owner can edit/delete
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Tip.objects.annotate(
        average_rating=Avg('rating__tip_rating'),
        number_times_saved=Count('author_saved_tip', distinct=True),
    ).order_by('-created_on')
    serializer_class = TipSerializer
