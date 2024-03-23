from django.shortcuts import render
from django.http import Http404

from .models import Notes

# Create your views here.

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':all_notes})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exit")
        
    return render(request, 'notes/notes_detail.html', {'note': note} )