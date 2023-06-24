from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TipAuthor
from .serializers import TipAuthorSerializer

# Create your views here.

class TipAuthorList(APIView):
    def get(self, request):
        tip_authors = TipAuthor.objects.all()
        serializer = TipAuthorSerializer(tip_authors, many=True)
        return Response(serializer.data)


