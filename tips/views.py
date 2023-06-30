from django.http import Http404
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tip
from .serializers import TipSerializer
from DRIVE.permissions import IsOwnerOrReadOnly


# Create your views here.
class TipList(APIView):
    serializer_class = TipSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):

        tips = Tip.objects.all()
        serializer = TipSerializer(
            tips, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TipSerializer(
            data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TipDetail(APIView):
    serializer_class = TipSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            tip = Tip.objects.get(pk=pk)
            self.check_object_permissions(self.request, tip)
            return tip
        except Tip.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tip = self.get_object(pk)
        serializer = TipSerializer(
            tip,
            context={'request': request})
        return Response(serializer.data)
    
    def put (self, request, pk):
        tip = self.get_object(pk)
        serializer = TipSerializer(
            tip, 
            data=request.data,
            context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, pk):
        tip = self.get_object(pk)
        tip.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )



