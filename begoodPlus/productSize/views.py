from django.shortcuts import render

from django.http import HttpResponse
import json

# Create your views here.
from productSize.models import ProductSize

def api_product_sizes(request, *args, **kwargs):
    all_sizes = ProductSize.objects.only("id", "size")
    sizes = []
    for p in all_sizes:
        size = {"id":p.id, "size": p.size}
        
        sizes.append(size)
    
    prep = {"productSizes": sizes}
    ret = HttpResponse(json.dumps(prep), content_type="application/json")
    return ret    