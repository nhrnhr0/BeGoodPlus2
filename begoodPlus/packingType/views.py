from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json

# Create your views here.
from packingType.models import PackingType
def api_packing_types(request, *args, **kwargs):
    all_packing = PackingType.objects.only("id", "name")
    pakcing_types = []
    for p in all_packing:
        packing_type = {"id":p.id, "name": p.name}
        
        pakcing_types.append(packing_type)
    
    prep = {"packingType": pakcing_types}
    ret = HttpResponse(json.dumps(prep), content_type="application/json")
    return ret    
