from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename="author")
router.register(r'notes', views.NoteViewSet, basename="note")
router.register(r'sub-genres', views.SubGenreViewSet,basename="sub-genre")
router.register(r'pub-info', views. PubInfoViewSet,basename="pub-info")
router.register(r'books', views.BookViewSet ,basename="book")

urlpatterns = [
    path('', include(router.urls))
]
