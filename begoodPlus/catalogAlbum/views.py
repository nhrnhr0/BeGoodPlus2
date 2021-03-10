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
def catalogView_api(request, *args, **wkrags):
    print('catalogView_api start')
    albums = CatalogAlbum.objects.prefetch_related('images').all()
    ser_context={'request': request}
    serializer = CatalogAlbumSerializer(albums,context=ser_context, many=True)
    data = json.dumps(serializer.data)
    context = {'catalogAlbumData':data,}
    print('catalogView_api end')
    return JsonResponse(context)
    #return render(request, 'catalog2.html', context=context)

def catalogView2(request, *args, **wkargs):
    print('catalogView2 start')
    albums = CatalogAlbum.objects.prefetch_related('images').all()
    context = {'albums':albums}
    print('catalogView2 end')
    return render(request, 'catalog2.html', context=context)
    