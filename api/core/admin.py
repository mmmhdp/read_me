from django.contrib import admin
from .models import Book, SubGenre, PubInfo, Author, Note

admin.site.register(SubGenre)
admin.site.register(Book)
admin.site.register(Note)
admin.site.register(PubInfo)
admin.site.register(Author)
