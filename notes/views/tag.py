# views.py
from rest_framework import generics
from taggit.models import Tag
from notes.serializers import TagSerializer

class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
