from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class BeseContactInformation(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    phone = models.CharField(verbose_name=_("phone"), max_length=30)
    email = models.EmailField(verbose_name=_('email'), max_length=120, blank=True, null=True)
    message = models.TextField(verbose_name=_('message'), max_length=1500, blank=True, null=True)