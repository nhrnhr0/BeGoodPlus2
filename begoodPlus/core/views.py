from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models.functions import Greatest
from django.contrib.postgres.search import TrigramSimilarity
from .models import UserSearchData
# Create your views here.
def admin_subscribe_view(request):
    webpush = {"group": 'admin' }
    return render(request, 'adminSubscribe.html',{"webpush":webpush})


def mainView(request, *args, **kwargs):
    return render(request, 'newMain.html', {})

from .forms import FormBeseContactInformation
def saveBaseContactFormView(request,next, *args, **kwargs):
    if request.method == "POST":
        form = FormBeseContactInformation(request.POST)
        if form.is_valid():
            form.save()
            print('form saved')

    return redirect(next)

from django.db.models import Q
import json
from catalogAlbum.models import CatalogAlbum, CatalogImage
from .serializers import SearchSummarySerializer, SearchCatalogImageSerializer,SearchCatalogAlbumSerializer
from itertools import chain 
from django.db.models import Value,CharField
from catalogAlbum.serializers import CatalogAlbumSerializer, CatalogImageSerializer

def get_session_key(request):
    if not request.session.session_key:
        request.session.save()
    return request.session.session_key


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('q', '')
        # albums_qs = CatalogAlbum.objects.filter(Q(title__icontains=q) & Q(is_public=True))
        
        products_qs = CatalogImage.objects.filter(
            Q(title__icontains=q) | 
            Q(description__icontains=q) |  
            Q(album__title__icontains=q) |
            Q(album__keywords__icontains=q)
            ).distinct()[0:20]
        '''
        threshold=0.3
        products_qs = CatalogImage.objects.annotate(
            similarity=Greatest(
                TrigramSimilarity('title', q), 
                TrigramSimilarity('description', q),
                TrigramSimilarity('images__title', q)
            )).filter(similarity__gte=threshold).order_by('-similarity')
        '''
        #print(albums_qs)
        print(products_qs)
        ser_context={'request': request}
        #albums = SearchCatalogAlbumSerializer(albums_qs,context=ser_context, many=True)
        products = SearchCatalogImageSerializer(products_qs,context=ser_context, many=True)

        #all = SearchSummarySerializer()
        #all.set_querylist([{'queryset': albums_qs, 'serializer_class': SearchCatalogAlbumSerializer},
        #                        {'queryset': products_qs, 'serializer_class': SearchCatalogImageSerializer}])
        #temp = all.get()
        #context = {'all':all}
        #return JsonResponse(context)
        #all = chain(albums, products)
        #all_rep = all.to_representation()
        
        #album_serializer = CatalogAlbumSerializer(albums_qs,context=ser_context, many=True)
        #album_data = json.dumps(album_serializer.data)

        #products_serializer = CatalogImageSerializer(products_qs,context=ser_context, many=True)
        #products_data = json.dumps(products_serializer.data)
        session = get_session_key(request)
        search_history = UserSearchData.objects.create(session=session, term=q, resultCount=len(products.data))
        search_history.save()

        context = {'all':products.data,
                    'id': search_history.id}
        #context = {'albums':album_data,
        #            'products': products_data}

        
        
        
        return JsonResponse(context)

from .models import UserSearchData
from django.contrib.contenttypes.models import ContentType

def autocompleteClick(request):
    print('autocompleteClick')
    if request.method == "POST":
        id = request.POST.get('id')
        my_type = request.POST.get('value[item][data][my_type]')
        content_id = request.POST.get('value[item][data][id]')
        if my_type == 'product':
            content_type = ContentType.objects.get_for_model(CatalogImage)
            obj = CatalogImage.objects.get(pk=content_id)
        elif my_type == 'album':
            content_type = ContentType.objects.get_for_model(CatalogAlbum)
            obj = CatalogAlbum.objects.get(pk=content_id)

        
        
        search_data = UserSearchData.objects.get(pk=id)
        search_data.content_object = obj
        search_data.save()
        context = {'status': 'ok',
                    'id':id}
        return JsonResponse(context)