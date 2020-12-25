from django.contrib import admin
from .models import FreeFlowClient
# Register your models here.
class freeFlowClientAdmin(admin.ModelAdmin):
    list_display = ('create_date', 'name', 'email','phone', 'country','message','privatePerson')
    
admin.site.register(FreeFlowClient,freeFlowClientAdmin)