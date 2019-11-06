# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from contextlib import contextmanager
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models import User
import json
import hashlib

# Create your views here.

def get_test_view(request):
    template = 'test_view.html'
    return render(request, template, {})

def home(request):
    template = 'home.html'
    return render(request, template, {})

def profile(request, user_id):
    template = 'profile.html'
    return render(request, template, {})
    

@csrf_exempt
def login(request):
    template = 'login.html'
    request_method = request.method

    if(request_method == 'GET'):
        return render(request, template, {})
    
    elif(request_method == 'POST'):
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        email_address = body['email']
        password = body['password']
        response = {}

        user  = User.objects.all() \
            .filter(email = email_address) \
            .filter(password_hash = hash_string(password)) \
            .first()

        if user:
            response = {
                'status': 'OK',
                'auth_key': user.auth_key,
                'email': user.email,
                'user_id': user.id
            }
        else:
            response = {
                'status': 'NOT FOUND'
            }

        return JsonResponse(response)

@csrf_exempt
def create_account(request):
    template = 'create_account.html'
    request_method = request.method

    if(request_method == 'GET'):
        return render(request, template, {})

    elif(request_method == 'POST'):
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        email_address = body['email']
        password = body['password']
        auth_key = hash_string(email_address + password)
        response = {}

        if account_exists(email_address):
            response = {
                'status': 'ACCOUNT EXISTS'
            }
        else:
            user = User(
                username = '',
                email = email_address,
                password_hash = hash_string(password),
                auth_key = auth_key
            )

            user.save()

            response = {
                'status': 'OK',
                'auth_key': auth_key,
                'email': email_address,
                'user_id': user.id
            }

        return JsonResponse(response)

def hash_string(input_string):
    hash_object = hashlib.md5(input_string.encode())
    return hash_object.hexdigest()

def account_exists(email_address):
    user  = User.objects.all() \
        .filter(email = email_address) \
        .first()

    if user:
        return True
    return False