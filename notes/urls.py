from django.urls import path
from notes.views import note, tag

# This is the list of the routes

app_name = "notes"

urlpatterns = [
    path('tags/', tag.TagListView.as_view(), name='tag-list'),
    path('lists-create/', note.NoteListCreateView.as_view(), name='note-list-create'),
    path('note/<int:pk>/', note.NoteRetrieveUpdateDestroyView.as_view(), name='note-retrieve-update-destroy'),
]