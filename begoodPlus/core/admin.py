from django.contrib import admin

# Register your models here.
from .models import UserSearchData
class UserSearchDataAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'term', 'resultCount', 'session')

admin.site.register(UserSearchData, UserSearchDataAdmin)