from django.http import Http404
from django.shortcuts import render
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tip
from .serializers import TipSerializer
from DRIVE.permissions import IsOwnerOrReadOnly


# Create your views here.
class TipList(generics.ListCreateAPIView):
    """
    List all tips
    Can create a new tip if logged in
    """
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    def perform_create (self, serializer):
        serializer.save(owner=self.request.user)


class TipDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves a specific tip
    Only owner can edit/delete
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
