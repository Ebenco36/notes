from notes.repositories.note_repository import NoteRepository
from rest_framework import serializers # Import the serializer class
from notes.models import Note # Import the Note model
from taggit.models import Tag
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def to_internal_value(self, data):
        tag, _ = Tag.objects.get_or_create(name=data)
        return tag

class NoteSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Note
        fields = ['id', 'title', 'body', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        note = Note.objects.create(**validated_data)

        for tag_data in tags_data:
            note.tags.add(tag_data)

        return note