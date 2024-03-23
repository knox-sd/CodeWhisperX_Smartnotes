from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes

# Class base view

class NoteListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NoteDetailsView(DetailView):
    model = Notes
    context_object_name = "note"


### Normal Views
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes':all_notes})

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exit")
        
#     return render(request, 'notes/notes_detail.html', {'note': note} )