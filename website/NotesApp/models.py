from django.db import models
from django.shortcuts import render

class Note(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='Notes/pdfs/')

def __str__(self):
    return self.title

def delete(self, *args, **kwargs):
    self.pdf.delete()
    self.cover.delete()
    super().delete(*args, **kwargs)
