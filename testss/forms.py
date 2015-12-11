#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: eastpiger
# @Date:   2015-12-11 15:42:09
# @Last Modified by:   eastpiger
# @Last Modified time: 2015-12-11 15:45:54
from django import forms

class MyAppWizardForm(forms.ModelForm):
    model = testss
    exclude = []
