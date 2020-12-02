from django.db import models
from django.utils.translation import gettext as _
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.
class CatalogImage(models.Model):

        
    title = models.CharField(max_length=120, verbose_name=_("title"), unique=True)
    description = models.TextField(verbose_name=_("description"))
    
    image = models.ImageField(verbose_name=_("image"))
    image_thumbnail = models.ImageField(verbose_name=_("image thumbnail"), null=True, blank=True)
    
    class Meta():
        verbose_name = _('Catalog image')
        verbose_name_plural = _('Catalog images')
        
    
    def save(self, *args, **kwargs):
        
        # if the image is set and and squere image we will generate one
        if self.image and not self.image_thumbnail:
            thub = Image.open(self.image)
            #thub.thumbnail(size)
            thub = thub.resize((450,450), Image.BILINEAR)
            f = BytesIO()
            try:
                thub.save(f, format='png')
                self.image_thumbnail.save('thunbnail_' + self.image.name,
                                                ContentFile(f.getvalue()))
            finally:
                f.close()

        
        super(CatalogImage, self).save(*args,**kwargs)
        
        
    def render_thumbnail(self, *args, **kwargs):
        ret = ''
        if self.image_thumbnail:
            ret += '<img src="%s" />' % (settings.MEDIA_URL + self.image_thumbnail.name) 
        return mark_safe(ret)
    render_thumbnail.short_description = _("thumbnail")
    
    def render_image(self, *args, **kwargs):
        ret = ''
        ret += '<img src="%s"/>' % (settings.MEDIA_URL + self.image.name) 
        return mark_safe(ret)
    render_image.short_description = _("image")
    
    def __str__(self):
        return self.title