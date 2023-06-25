from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TipAuthor
from .serializers import TipAuthorSerializer
from DRIVE.permissions import IsOwnerOrReadOnly

# Create your views here.

class TipAuthorList(APIView):
    def get(self, request):
        tip_authors = TipAuthor.objects.all()
        serializer = TipAuthorSerializer(
            tip_authors, 
            many=True, 
            context={'request': request})
        return Response(serializer.data)


class TipAuthorDetail(APIView):
    serializer_class = TipAuthorSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_author(self, pk):
        try:
            author = TipAuthor.objects.get(pk=pk)
            self.check_object_permissions(self.request, author)
            return author
        except TipAuthor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        author = self.get_author(pk)
        serializer = TipAuthorSerializer(
            author,
            context={'request': request})
        return Response(serializer.data)
    
    def put (self, request, pk):
        author = self.get_author(pk)
        serializer = TipAuthorSerializer(
            author, 
            data=request.data,
            context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



