from rest_framework import serializers

from .models import CatalogImage

class CatalogImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogImage
        fields = '__all__'