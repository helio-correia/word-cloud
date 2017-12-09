from rest_framework import generics, permissions

from .models import Word
from .serializers import WordSerializer


class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = (permissions.IsAuthenticated, )
