from django.shortcuts import render

# Create your views here.
from .models import Color
from .serializers import ColorSerializer
from rest_framework import viewsets
class ColorsViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
