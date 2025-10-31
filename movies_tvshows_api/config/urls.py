from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieViewSet
from tvshows.views import TVShowViewSet
from .auth_views import RegisterView, LoginView

# ViewSet Routers
router = DefaultRouter()
router.register(r'api/movies', MovieViewSet, basename='movie')
router.register(r'api/tvshows', TVShowViewSet, basename='tvshow')

urlpatterns = [
    path('admin/', admin.site.urls),
    # ViewSet Routes (Router)
    path('', include(router.urls)),
    # Absolute style-based routes for demo styles
    path('', include('movies.urls')),
    path('', include('tvshows.urls')),
    # Auth
    path('api/auth/login/', LoginView.as_view(), name='api-login'),
    path('api/auth/register/', RegisterView.as_view(), name='api-register'),
]
