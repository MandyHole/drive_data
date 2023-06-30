from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tip
from .serializers import TipSerializer


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
