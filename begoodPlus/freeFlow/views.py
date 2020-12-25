from django.shortcuts import render

# Create your views here.

from .forms import freeFlowClientForm
from utils import utils

from webpush import send_group_notification
from django.urls import reverse

import threading, time

def freeFlowView(request):
    if request.method == 'POST':
        form = freeFlowClientForm(request.POST)
        if form.is_valid():
            #print(form)
            obj = form.save()
            name = obj.name
            email = obj.email
            phone = obj.phone
            country = obj.country
            message = obj.message
            #obj = form.instance
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id] )
            payload = {"head": "Free Flow", "body": message, "icon": "https://ms-global.co.il/static/assets/freeFlow/assets/img/freeFlowFirstImage.png", "url": url}
            thread = threading.Thread(target=send_group_notification, kwargs={"group_name":"admin", "payload":payload, "ttl":1000})
            thread.start()

    return render(request, 'freeflow2.html',{})