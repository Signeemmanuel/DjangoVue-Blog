from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet, UserViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
]