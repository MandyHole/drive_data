from rest_framework import generics, permissions
from drive_api.permissions import IsOwnerOrReadOnly
from .models import SavedTip
from .serializers import SavedTipSerializer

class SavedTipList(generics.ListCreateAPIView):
    serializer_class = SavedTipSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = SavedTip.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SavedTipDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavedTipSerializer
    queryset = SavedTip.objects.all()

