from core.models import *
from core.serializers import *
from rest_framework import generics, viewsets

class SubGenreViewSet(viewsets.ModelViewSet):
    queryset = SubGenre.objects.all()
    serializer_class = SubGenreSerializer

class PubInfoViewSet(viewsets.ModelViewSet):
    queryset = PubInfo.objects.all()
    serializer_class = PubInfoSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
