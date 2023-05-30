from .models import Book, SubGenre, PubInfo, Author, Note
from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    note = serializers.PrimaryKeyRelatedField(many=True,
                                              queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'note']


class PubInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PubInfo
        fields = ['publisher', 'year']


class SubGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGenre
        fields = ['name', 'description']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'second_n', 'last_n', 'alias']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, required=True)
    sub_genre = SubGenreSerializer()
    pub_info = PubInfoSerializer()

    class Meta:
        model = Book
        fields = ['title', 'summary', 'global_genre', 'sub_genre', 'pub_info', 'author', 'pub_info']

    def create(self, validated_data):
        sub_genre_data = validated_data.pop('sub_genre')
        pub_info_data = validated_data.pop('pub_info')

        authors_data = validated_data.pop('author')

        sub_genre, created_sub_genre = SubGenre.objects.update_or_create(sub_genre_data)
        pub_info, created_pub_info = PubInfo.objects.update_or_create(pub_info_data)

        authors = []
        for author_data in authors_data:
            author, created_author = Author.objects.update_or_create(author_data)
            authors.append(author)

        book, created = Book.objects.update_or_create(sub_genre=sub_genre,
                                                      pub_info=pub_info,
                                                      **validated_data)

        book.author.set(authors)

        return book


class NoteSerializer(serializers.ModelSerializer):
    related_paper = BookSerializer()
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ['related_paper', 'review', 'rate', 'owner']

    def create(self, validated_data):
        review = validated_data.pop('review')
        rate = validated_data.pop('rate')
        related_paper_data = validated_data.pop('related_paper')

        related_paper = BookSerializer.create(BookSerializer, related_paper_data)

        note, created = Note.objects.update_or_create(
            related_paper=related_paper,
            review=review,
            rate=rate,
            **validated_data
        )
        return note
