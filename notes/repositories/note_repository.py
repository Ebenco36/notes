from notes.models import Note

class NoteRepository:
    @staticmethod
    def create(user, title, body, tags=None):
        note = Note.objects.create(user=user, title=title, body=body)
        """
            We are adding records on relationship created within our 
            model for note. 
            Note: that this is not compulsory.
        """
        if tags:
            note.tags.set(tags)

        return note

    @staticmethod
    def get_note_by_id(note_id):
        try:
            return Note.objects.prefetch_related('tags').get(id=note_id)
        except Note.DoesNotExist:
            return None
        
    
    @staticmethod
    def filter_note(queryFilter):
        return Note.objects.prefetch_related('tags').filter(queryFilter)

    @staticmethod
    def update(note, title, body, tags = None):
        print(tags)
        note.title = title
        note.body = body
        if tags:
            note.tags.set(tags)
        note.save()
        return note

    @staticmethod
    def delete(note):
        note.delete()

    @staticmethod
    def list_by_owner(user):
        return Note.objects.prefetch_related('tags').filter(user=user)

    @staticmethod
    def list_all():
        records = Note.objects.prefetch_related('tags').all()
        return records
