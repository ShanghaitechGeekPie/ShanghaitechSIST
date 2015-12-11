#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: eastpiger
# @Date:   2015-12-11 15:40:01
# @Last Modified by:   eastpiger
# @Last Modified time: 2015-12-11 15:42:26
# my_apps/cms_wizards.py

from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from .forms import MyAppWizardForm
from .models import MyApp

class MyAppWizard(Wizard):
    pass

my_app_wizard = MyAppWizard(
    title="New MyApp",
    weight=200,
    form=MyAppWizardForm,
    description="Create a new MyApp instance",
)

wizard_pool.register(my_app_wizard)
