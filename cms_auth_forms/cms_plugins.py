#!/bin/env python
# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models import CMSPlugin
from django.utils.translation import ugettext as _

from django.contrib.auth.forms import AuthenticationForm

class LoginFormPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _(u"Плагин формы логина")
    cache = False
    module = _(u'Аутентификация')

    def render(self, context, instance, placeholder):
        # pylint: disable=E1101
        request = self.context['request']

        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST, files=request.FILES)
        else:
            form = AuthenticationForm()

        context['form'] = form

plugin_pool.register_plugin(LoginFormPlugin)
