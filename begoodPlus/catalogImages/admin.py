from django.contrib import admin

from .models import CatalogImage
# Register your models here.
class CatalogImageAdmin(admin.ModelAdmin):
    list_display = ('render_thumbnail', 'title', 'description',)
    readonly_fields = ('render_thumbnail', 'render_image',)
    search_fields = ('title',)

admin.site.register(CatalogImage,CatalogImageAdmin)