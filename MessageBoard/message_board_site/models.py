# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)

class MessageBoardPost(models.Model):
    content = models.CharField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)