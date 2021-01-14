from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from .forms import NoteForm
from .models import Note
from django.urls import reverse_lazy

def home(request):
    template_name = 'index.html'
    return render(request, 'index.html')

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {
        'notes': notes
    })

def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'upload_note.html', {
        'form': form
    })

def delete_note(request, pk):
    if request.method == 'POST':
        note = Note.objects.get(pk=pk)
        note.delete()
    return redirect('note_list')

def search(request):
    allnotes = Note.objects.all()
    params = {'allnotes': allnotes}
    return render(request, 'search.html')
    