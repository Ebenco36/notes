from notes.repositories.note_repository import NoteRepository
from rest_framework import serializers # Import the serializer class
from notes.models import Note # Import the Note model
from taggit.models import Tag
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class NoteSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Note.tags.all(),
        slug_field='name'
    )
    class Meta:
        model = Note
        fields = ['id', 'user', 'title', 'body', 'tags', 'created', 'updated']


class CreateNoteSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=255), write_only=True)
    class Meta:
        model = Note
        fields = ['title', 'body', 'tags']
