# -*- coding: utf-8 -*-
#
from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import Alias, Asset

__all__ = ['AliasForm']


class AliasForm(forms.ModelForm):
    asset = forms.ModelChoiceField(
        queryset=Asset.objects.all(), label=_('Asset'), required=True,
        widget=forms.Select(
            attrs={'class': 'select2', 'data-placeholder': _('Select asset')}
        )
    )

    class Meta:
        model = Alias
        fields = ['name', 'asset']

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance', None):
            initial = kwargs.get('initial', {})
            initial['asset'] = kwargs['instance'].asset
        super().__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     alias = super().save(commit=commit)
    #     assets = self.cleaned_data['assets']
    #     alias.assets.set(assets)
    #     return alias
