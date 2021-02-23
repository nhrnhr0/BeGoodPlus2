from rest_framework import serializers

from .models import ProductSize
class ProductSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'