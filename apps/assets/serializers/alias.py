# -*- coding: utf-8 -*-
#
from rest_framework import serializers
from rest_framework_bulk.serializers import BulkListSerializer

from ..models import Alias


class AliasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alias
        fields = ("id", "name", "asset_info")
        list_serializer_class = BulkListSerializer

