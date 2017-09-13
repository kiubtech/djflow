from django.db import models
from django.utils.translation import ugettext as _

from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='djflow')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = _("Configuración del sitio")

