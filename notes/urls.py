from django.urls import path
from notes.views import note
from notes.views.tag import TagRetrieveUpdateDestroyView, TagListCreateView 

# This is the list of the routes

app_name = "notes"

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list'),
    path('tags/<int:tag_id>/', TagRetrieveUpdateDestroyView.as_view(), name='tag-detail'),
    path('lists/', note.NoteListCreateView.as_view(), name='note-list-create'),
    path('note/<int:pk>/', note.NoteRetrieveUpdateDestroyView.as_view(), name='note-retrieve-update-destroy'),
]