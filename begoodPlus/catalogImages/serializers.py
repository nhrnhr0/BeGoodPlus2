from rest_framework import serializers

from .models import CatalogImage

class CatalogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogImage
        fields = '__all__'
        #exclude = ('images',)