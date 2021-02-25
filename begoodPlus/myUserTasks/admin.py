from django.contrib import admin

# Register your models here.
from .models import ContactFormTask
class ContactFormTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'session','task_name', 'created_date','modified_date','name','phone','email', 'message', 'url')
    
admin.site.register(ContactFormTask, ContactFormTaskAdmin)