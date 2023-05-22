from core.models import Note, Author, Book, SubGenre, PubInfo
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
        fields = ['publisher','year']


class SubGenreSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SubGenre 
        fields = ['name','description']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Author 
        fields = ['name','second_n','last_n','alias']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required = True, many = True)
    sub_genre = SubGenreSerializer() 
    pub_info = PubInfoSerializer()

    class Meta: 
        model = Book
        fields = ['title','summary','global_genre', 'sub_genre', 'pub_info','author']
    
    def create(self, validated_data):
        title = validated_data.pop('title')
        summary = validated_data.pop('summary')
        global_genre = validated_data.pop('global_genre') 

        author_data = validated_data.pop('author')
        sub_genre_data = validated_data.pop('sub_genre') 
        pub_info_data = validated_data.pop('pub_info')
        
        author = AuthorSerializer.create(AuthorSerializer,
                                         validated_data = author_data)
        sub_genre = SubGenreSerializer.create(SubGenreSerizalier,
                                              validated_date = sub_genre_data)
        pub_info = PubInfoSerializer.create(PubInfoSerializer,
                                            validated_data = pub_info_data)
        book, created = Book.objects.update_or_create(
                    author=author,title=title,summary=summary,global_genre=global_genre,
                    sub_genre=sub_genre,pub_info=pub_info
                    )
        return book


class NoteSerializer(serializers.ModelSerializer):
    related_paper = BookSerializer()
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta: 
        model = Note
        fields = ['related_paper','review','rate','owner']
    
    def create(self, validated_data):
        review = validate_data.pop('review')
        rate = validate_data.pop('rate')
        
        related_paper_data = validate_data.pop('related_paper')
        related_paper = BookSerizalizer.create(BookSerializer(),
                                               validated_data = realated_paper_data)
        note, created = Note.objects.update_or_create(
                related_paper = related_paper,
                review = review,
                rate = rate,
                )
        return note





