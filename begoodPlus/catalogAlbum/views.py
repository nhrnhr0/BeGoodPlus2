from django.shortcuts import render

# Create your views here.
from catalogAlbum.models import CatalogAlbum
from .serializers import CatalogAlbumSerializer
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

class CatalogAlbumViewSet(viewsets.ModelViewSet):
    queryset = CatalogAlbum.objects.all()
    serializer_class = CatalogAlbumSerializer


import json

def catalogView2(request, *args, **wkargs):
    albums = CatalogAlbum.objects.prefetch_related('images').all()
    ser_context={'request': request}
    serializer = CatalogAlbumSerializer(albums,context=ser_context, many=True)
    #content = JSONRenderer().render(serializer.data)
    data = json.dumps(serializer.data)
    #context = {'catalogAlbums': albums,'catalogAlbumData':data}
    context = {'catalogAlbumData':data}
    #context = {'catalogAlbums': albums,}
    return render(request, 'catalog2.html', context=context)
    