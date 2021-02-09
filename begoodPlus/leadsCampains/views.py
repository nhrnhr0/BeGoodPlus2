from django.shortcuts import render

# Create your views here.
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def TaxReturnCampainView(request):
    context = {}
    return render(request=request, template_name='taxReturnLead.html', context=context)