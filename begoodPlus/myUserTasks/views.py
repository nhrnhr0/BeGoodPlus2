from django.shortcuts import render, HttpResponse
from django.contrib.sessions.models import Session
from django.db import IntegrityError

# Create your views here.
def updateUserTaskView(request, *args, **kwargs):
    print('request', request)
    
from .models import ContactFormTask, UserTask
import json
from django.core.exceptions import ObjectDoesNotExist

def updateContactFormUserTaskView(request,*args, **kwargs):
    if request.is_ajax() and request.method == "POST":
        #task_id = request.POST.get('task_id', None)
        task_name = request.POST.get('taskName', None)
#        if task_name:
#            try:
#                task = ContactFormTask.objects.get(task_name=task_name)
#            except ObjectDoesNotExist:
#                task = ContactFormTask(task_name=task_name)
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('email', None)
        message = request.POST.get('message', None)
        url = request.META['HTTP_REFERER']
        session = request.session.session_key
        #form = ContactFormTask(task_name=task_name, session=session, name=name, phone=phone, email=email, message=message, url=url)
        #data = form.save()
        #try:
        #    task = ContactFormTask(name=name, phone=phone, email=email, message=message, url=url, session=session)
        #except IntegrityError as e:
        #    task = ContactFormTask.objects.get(task_name=task_name)
        #    task.name = name
        #    task.phone = phone
        #    task.email = email
        #    task.
        #    task.save()
        task, created = ContactFormTask.objects.get_or_create(task_name=task_name)
        task.session=session
        task.name=name
        task.email=email
        task.phone=phone
        task.message=message
        task.url=url
        task.save()
        print(created, task.id,task)
        

        return HttpResponse(json.dumps({'task_id': task.id}), content_type="application/json")
        #return HttpResponse(json.dumps({'task_id': form.id}, con="application/json"))

    pass