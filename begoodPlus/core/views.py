from django.shortcuts import render,redirect
from django.http import JsonResponse

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
from catalogAlbum.serializers import CatalogAlbumSerializer, CatalogImageSerializer
def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('q', '')
        albums_qs = CatalogAlbum.objects.filter(Q(title__icontains=q) & Q(is_public=True))
        products_qs = CatalogImage.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
        print(albums_qs)
        print(products_qs)
        ser_context={'request': request}

        album_serializer = CatalogAlbumSerializer(albums_qs,context=ser_context, many=True)
        album_data = json.dumps(album_serializer.data)

        products_serializer = CatalogImageSerializer(products_qs,context=ser_context, many=True)
        products_data = json.dumps(products_serializer.data)

        context = {'albums':album_data,
                    'products': products_data}
        return JsonResponse(context)