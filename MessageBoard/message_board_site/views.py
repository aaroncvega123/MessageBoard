# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from contextlib import contextmanager

# Create your views here.

class TestView():
    def __init__(self, request):
        self.template_name = 'test_view.html'
        self.request = request

    def get(self, request):
        print("self request")
        print(self.request)
        return render(self.request, self.template_name, {})

def get_test_view(request):
    template = 'test_view.html'
    return render(request, template, {})