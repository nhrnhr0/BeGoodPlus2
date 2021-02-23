from rest_framework import serializers

from .models import CatalogAlbum
from catalogImages.serializers import CatalogImageSerializer

class CatalogAlbumSerializer(serializers.HyperlinkedModelSerializer):
    images_list = serializers.SerializerMethodField('_get_images')
    def _get_images(self, obj):
        serializer = CatalogImageSerializer(obj.images, many=True)
        return serializer.data
    class Meta:
        model = CatalogAlbum
        #fields = '__all__'
        exclude = ('images',)