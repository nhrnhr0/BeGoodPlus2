from django.db import models

from product.models import Product
from django.utils.translation import gettext as _

# Create your models here.
class GlofaType(models.Model):
    class Meta:
        verbose_name = _('glofa type')
        verbose_name_plural = _('glofa types')
    num = models.PositiveIntegerField(verbose_name=_("number"));
    description = models.TextField(verbose_name=_("description"));
    supportedProducts = models.ManyToManyField(to=Product, verbose_name=_("supported products"), related_name='supportedProducts')
    
    def __str__(self):
        return str(self.num) + ') ' + self.description