from django.shortcuts import render
from .models import CatalogImage
from rest_framework import viewsets
from .serializers import CatalogImageSerializer

# Create your views here.
class CatalogImageViewSet(viewsets.ModelViewSet):
    queryset = CatalogImage.objects.all()
    serializer_class = CatalogImageSerializer