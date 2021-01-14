from django.db import models
from django.shortcuts import render
import os
from pymongo import settings

class Note(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    allfiles = models.FileField(upload_to='Notes/allfiles/')

def __str__(self):
    return self.title

def delete(self, *args, **kwargs):
    self.allfiles.delete()
    super().delete(*args, **kwargs)
