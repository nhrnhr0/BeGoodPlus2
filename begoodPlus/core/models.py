from django.db import models
from django.utils.translation import gettext as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class BeseContactInformation(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    phone = models.CharField(verbose_name=_("phone"), max_length=30)
    email = models.EmailField(verbose_name=_('email'), max_length=120, blank=True, null=True)
    message = models.TextField(verbose_name=_('message'), max_length=1500, blank=True, null=True)


class UserSearchData(models.Model):
    session = models.CharField(max_length=50)
    term = models.CharField(max_length=50)
    resultCount = models.IntegerField(verbose_name=_('number of results'))
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
