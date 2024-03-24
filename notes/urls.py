from django.urls import path

from . import views

urlpatterns = [
    # path('notes', views.list),
    # path('notes/<int:pk>', views.detail),

    path('notes', views.NoteListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NoteDetailsView.as_view(), name="notes.detail"),
]