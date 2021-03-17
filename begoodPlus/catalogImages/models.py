from django.db import models
from django.utils.translation import gettext as _
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.html import mark_safe
from django.conf import settings

from color.models import Color
from productSize.models import ProductSize
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.
class CatalogImage(models.Model):

        
    title = models.CharField(max_length=120, verbose_name=_("title"), unique=True)
    description = models.TextField(verbose_name=_("description"))
    
    image = models.ImageField(verbose_name=_("image"))
    image_thumbnail = models.ImageField(verbose_name=_("image thumbnail"), null=True, blank=True)

    colors = models.ManyToManyField(to=Color)
    sizes = models.ManyToManyField(to=ProductSize)
    
    class Meta():
        verbose_name = _('Catalog image')
        verbose_name_plural = _('Catalog images')
        ordering = ['throughimage__image_order'] 
        
    
    def optimize_image(image,size, *args, **kwargs):
        im = Image.open(image)
        output = BytesIO()
        im = im.resize(size)
        im = im.convert('RGB')
        im.save(output, format='JPEG', quality=75)
        output.seek(0)
        return output 
    
    def save(self, *args, **kwargs):
        if self.image:
            output = CatalogImage.optimize_image(self.image, size=(923, 715))
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)
            output2 = CatalogImage.optimize_image(self.image, size=(450,450))
            self.image_thumbnail = InMemoryUploadedFile(output2, 'ImageField', "image_thumbnail_%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output2), None)
        # if the image is set and and squere image we will generate one
        '''
        im = Image.open(self.image)
        im2 = Image.open(self.image)
        output = BytesIO()
        output2 = BytesIO()

        # Resize/modify the image
        im = im.resize((923, 715))
        im2 = im2.resize((450, 450))
        im = im.convert('RGB')
        im2 = im2.convert('RGB')

        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=75)
        im2.save(output2, format='JPEG', quality=75)
        output.seek(0)
        output2.seek(0)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)
        self.image_thumbnail = InMemoryUploadedFile(output2, 'ImageField', "image_thumbnail_%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output2), None)
        print(self.image, self.image.size)
        print(self.image_thumbnail, self.image_thumbnail.size)
        '''
        '''
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
        '''
        
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