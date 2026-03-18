from django.shortcuts import render
from django.conf import settings
import rest_framework
from rest_framework import  viewsets

from .models import MusicMedia
from .serializers import MusicMediaSerializer


class MusicMediaViewSet(viewsets.ModelViewSet):
    queryset = MusicMedia.objects.all()
    serializer_class = MusicMediaSerializer
