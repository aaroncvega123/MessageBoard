# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from contextlib import contextmanager

# Create your views here.

def get_test_view(request):
    template = 'test_view.html'
    return render(request, template, {})

def get_login_view(request):
    template = 'login.html'
    return render(request, template, {})