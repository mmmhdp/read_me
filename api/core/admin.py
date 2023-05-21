from django.contrib import admin
from core.models import Note, Author, SubGenre, PubInfo, Book
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Note)
admin.site.register(PubInfo)
admin.site.register(SubGenre)
