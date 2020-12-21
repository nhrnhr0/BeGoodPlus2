from django.contrib import admin
from .models import FreeFlowClient
# Register your models here.
class freeFlowClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone', 'country','message',)
    
admin.site.register(FreeFlowClient,freeFlowClientAdmin)