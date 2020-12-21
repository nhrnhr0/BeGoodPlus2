from django.shortcuts import render

# Create your views here.

from .forms import freeFlowClientForm

def freeFlowView(request):
    if request.method == 'POST':
        form = freeFlowClientForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
    return render(request, 'freeflow2.html',{})