from django.shortcuts import render
from .models import NotesApp

from django.http import HttpResponse

def index(request):
    return HttpResponse(index)

