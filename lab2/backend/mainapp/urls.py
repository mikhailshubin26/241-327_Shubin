from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicMediaViewSet

router = DefaultRouter()
router.register(r'musicmedia', MusicMediaViewSet, basename='musicmedia')

urlpatterns = [
    path('', include(router.urls)),
]