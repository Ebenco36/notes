from notes.repositories.note_repository import NoteRepository
from rest_framework import serializers # Import the serializer class
from notes.models import Note, Tag # Import the Note model

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')



class NoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Note
        fields = ['id', 'user', 'title', 'body', 'tags', 'created', 'updated']
