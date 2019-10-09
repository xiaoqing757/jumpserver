from django.db import models

import logging
from django.utils.translation import ugettext_lazy as _
from .asset import Asset


__all__ = ['Alias']
logger = logging.getLogger(__name__)


class Alias(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="aliases")
    name = models.CharField(max_length=63, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_('Date created'))

    def __str__(self):
        return self.name

    @property
    def asset_info(self):
        return {"hostname": self.asset.hostname, "id": self.asset.id}
