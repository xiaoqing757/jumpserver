# ~*~ coding: utf-8 ~*~

from rest_framework_bulk import BulkModelViewSet
from django.db.models import Count

from common.utils import get_logger
from ..hands import IsSuperUser
from ..models import Alias
from .. import serializers


logger = get_logger(__file__)
__all__ = ['AliasViewSet']


class AliasViewSet(BulkModelViewSet):
    queryset = Alias.objects.all()
    permission_classes = (IsSuperUser,)
    serializer_class = serializers.AliasSerializer


