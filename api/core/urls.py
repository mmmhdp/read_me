from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="READ_ME API",
        default_version='v1',
        description="API for a reading diary like app",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()

router.register(r'users', views.UserViewSet, basename="user")

router.register(r'authors', views.AuthorViewSet, basename="author")
router.register(r'notes', views.NoteViewSet, basename="note")
router.register(r'sub-genres', views.SubGenreViewSet, basename="sub-genre")
router.register(r'pub-info', views.PubInfoViewSet,basename="pub-info")
router.register(r'books', views.BookViewSet, basename="book")

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
    path('accounts/', include('rest_registration.api.urls')),
]
