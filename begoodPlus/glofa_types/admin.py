from django.contrib import admin
from glofa_types.models import GlofaType
# Register your models here.
class GlofaTypeAdmin(admin.ModelAdmin):
    list_display = ('num','description',)
    autocomplete_fields = ('supportedProducts',)

admin.site.register(GlofaType,GlofaTypeAdmin)