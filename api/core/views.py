from .serializers import *
from .models import Book, SubGenre, PubInfo, Author, Note
from rest_framework import viewsets
from django.contrib.auth.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubGenreViewSet(viewsets.ModelViewSet):
    serializer_class = SubGenreSerializer

    def get_queryset(self):
        queryset = SubGenre.objects.all().filter(book__note__owner_id=self.request.user.id)
        return queryset


class PubInfoViewSet(viewsets.ModelViewSet):
    serializer_class = PubInfoSerializer

    def get_queryset(self):
        queryset = PubInfo.objects.all().filter(book__note__owner_id=self.request.user.id)
        return queryset


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all().filter(book__note__owner_id=self.request.user.id)
        return queryset


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all().filter(note__owner_id=self.request.user.id)
        return queryset


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all().filter(owner_id=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
