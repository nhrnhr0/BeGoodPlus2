from rest_framework import serializers

from .models import CatalogImage
from color.serializers import ColorSerializer
from productSize.serializers import ProductSizeSerializer
class CatalogImageSerializer(serializers.HyperlinkedModelSerializer):

    colors_list = serializers.SerializerMethodField('_get_colors')
    id = serializers.IntegerField(read_only=True)
    def _get_colors(self, obj):
        serializer = ColorSerializer(obj.colors,context=self.context, many=True)
        return serializer.data
    sizes_list = serializers.SerializerMethodField('_get_sizes')
    def _get_sizes(self, obj):
        serializer = ProductSizeSerializer(obj.sizes,context=self.context, many=True)
        return serializer.data


    class Meta:
        model = CatalogImage
        #fields = '__all__'
        exclude = ('colors','sizes')