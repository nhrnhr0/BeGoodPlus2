from django.shortcuts import render

# Create your views here.
from catalogAlbum.models import CatalogAlbum
#from catalogImages.models import CatalogImage
def catalogView2(request, *args, **wkargs):
    albums = CatalogAlbum.objects.all()
    #images = CatalogImage.objects.all().order_by('album')
    context = {'catalogAlbums': albums}
    return render(request, 'catalog2.html', context=context)