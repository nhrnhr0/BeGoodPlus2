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

from django.db.models.query import QuerySet
from pprint import PrettyPrinter

def dprint(object, stream=None, indent=1, width=80, depth=None):
    """
    A small addition to pprint that converts any Django model objects to dictionaries so they print prettier.

    h3. Example usage

        >>> from toolbox.dprint import dprint
        >>> from app.models import Dummy
        >>> dprint(Dummy.objects.all().latest())
         {'first_name': u'Ben',
          'last_name': u'Welsh',
          'city': u'Los Angeles',
          'slug': u'ben-welsh',
    """
    # Catch any singleton Django model object that might get passed in
    if getattr(object, '__metaclass__', None):
        if object.__metaclass__.__name__ == 'ModelBase':
            # Convert it to a dictionary
            object = object.__dict__
    
    # Catch any Django QuerySets that might get passed in
    elif isinstance(object, QuerySet):
        # Convert it to a list of dictionaries
        object = [i.__dict__ for i in object]
        
    # Pass everything through pprint in the typical way
    printer = PrettyPrinter(stream=stream, indent=indent, width=width, depth=depth)
    printer.pprint(object)


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

from django.db.models import Max
def catalogView2(request, *args, **wkargs):

    print('catalogView2 start')
    albums = CatalogAlbum.objects.prefetch_related('images')#.annotate(max_weight=Max('throughimage__image_order')).order_by('-max_weight').all()#.order_by("throughimage__image_order")
    #albums = albums.order_by('id', 'throughimage__image_order')
    #albums.images.order_by('throughimage__image_order')
    context = {'albums':albums}
    print('catalogView2 end')
    return render(request, 'catalog2.html', context=context)
    