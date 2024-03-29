from django.shortcuts import render
from django.http import Http404 #if the page not found or page doesn't exist
from django.views.generic import CreateView, DetailView, ListView

from .models import Notes

# Class base view
class NoteCreateView(CreateView): #Apply CRUD
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'

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