from django.db import models


from django.utils.translation import gettext as _

# Create your models here.
class FreeFlowClient(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=50, verbose_name=_('telephone'))
    country = models.CharField(max_length=50, verbose_name=_('country'))
    message = models.CharField(max_length=200, verbose_name=_('message'))
    privatePerson = models.BooleanField(verbose_name=_("is private person"),default=True)
    create_date = models.DateTimeField(verbose_name=_("create date"), auto_now_add=True)