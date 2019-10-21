# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    auth_key = models.CharField(max_length=255, default=None)

class MessageBoardPost(models.Model):
    content = models.CharField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class InstitutionType(models.Model):
    type_name = models.CharField(max_length=1000)

class Institution(models.Model):
    name = models.CharField(max_length=1000)
    type_id = models.ForeignKey(InstitutionType)

class Instructor(models.Model):
    name = models.CharField(max_length=1000)

class Course(models.Model):
    name = models.CharField(max_length=1000)
    instructor = models.ForeignKey(Instructor)
    institution = models.ForeignKey(Institution)

class ClassNotes(models.Model):
    created_by = models.ForeignKey(User)
    title = models.CharField(max_length=1000)
    course_id = models.ForeignKey(Course)
