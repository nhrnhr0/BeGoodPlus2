from django.db import models
# Create your models here.
from django.utils.translation import gettext as _

from catalogImages.models import CatalogImage
from django.utils.html import mark_safe

'''
class CatalogAlbum(models.Model):
    title = models.CharField(max_length=120, verbose_name=_("title"))
    slug = models.SlugField(max_length=120, verbose_name=_("slug"))
    images = models.ManyToManyField(to=CatalogImage, related_name='images', blank=True, through='ThroughImage')# 
    
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('slug', 'parent',)   
        

    
    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    #def __str__(self):
    #    return self.title
    
    def get_absolute_url(self, *args, **kwargs):
        from django.urls import reverse
        parent = self.parent
        full_slug = ''
        while parent != None:
            full_slug = parent.slug + '/' + full_slug
            parent = parent.parent
        full_slug = full_slug + '/' + self.slug
        return reverse('albumView', args=[full_slug])
    get_absolute_url.short_description = 'URL'

'''
from mptt.models import MPTTModel, TreeForeignKey

class CatalogAlbum(MPTTModel):
    title = models.CharField(max_length=120, verbose_name=_("title"))
    slug = models.SlugField(max_length=120, verbose_name=_("slug"))
    images = models.ManyToManyField(to=CatalogImage, related_name='images', blank=True, through='ThroughImage')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']
        
    class Meta:
        unique_together = ('slug', 'parent',)   
    def __str__(self):
        return self.title
        
    def get_absolute_url(self, *args, **kwargs):
        from django.urls import reverse
        parent = self.parent
        full_slug = ''
        while parent != None:
            full_slug = parent.slug + '/' + full_slug
            parent = parent.parent
        full_slug = full_slug  + self.slug
        if full_slug == '':
            return ''
        return reverse('albumView', args=[full_slug])
    get_absolute_url.short_description = 'URL'

    def view_in_website_link(self, *args, **kwargs):
        ret = '<a href="%s"> צפייה באתר %s</a>' %(self.get_absolute_url(), self.title)
        return mark_safe(ret)
    view_in_website_link.short_description = _("view in website")
        #return ret
    

from adminsortable.fields import SortableForeignKey
from adminsortable.models import Sortable

class ThroughImage(Sortable):
    #catalogImage = models.ForeignKey(CatalogImage, on_delete=models.CASCADE)
    catalogImage = SortableForeignKey(CatalogImage, on_delete=models.CASCADE)
    catalogAlbum = models.ForeignKey(CatalogAlbum, on_delete=models.CASCADE)
    #weight = models.IntegerField(verbose_name=_("weight"))
    
    class Meta(Sortable.Meta):
        #ordering = ['weight']
        #unique_together = ('catalogAlbum', 'weight',)
        pass

