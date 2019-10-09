# -*- coding: utf-8 -*-
#

from django.views.generic import TemplateView, CreateView, \
    UpdateView, DeleteView, DetailView
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy

from common.mixins import AdminUserRequiredMixin
from common.const import create_success_msg, update_success_msg
from ..models import Alias
from ..forms import AliasForm, LabelForm


__all__ = (
    "AliasListView", "AliasCreateView", "AliasUpdateView",
    "AliasDetailView", "AliasDeleteView",
)


class AliasListView(AdminUserRequiredMixin, TemplateView):
    template_name = 'assets/alias_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('别名列表'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class AliasCreateView(AdminUserRequiredMixin, CreateView):
    model = Alias
    template_name = 'assets/alias_create_update.html'
    form_class = AliasForm
    success_url = reverse_lazy('assets:alias-list')
    success_message = create_success_msg

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('创建别名'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class AliasUpdateView(AdminUserRequiredMixin, UpdateView):
    model = Alias
    template_name = 'assets/alias_create_update.html'
    form_class = AliasForm
    success_url = reverse_lazy('assets:alias-list')
    success_message = update_success_msg

    def get_context_data(self, **kwargs):
        context = {
            'app': _('Assets'),
            'action': _('更新别名'),
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class AliasDetailView(AdminUserRequiredMixin, DetailView):
    pass


class AliasDeleteView(AdminUserRequiredMixin, DeleteView):
    model = Alias
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('assets:alias-list')
