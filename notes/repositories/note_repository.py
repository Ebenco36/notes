from notes.models import Note

class NoteRepository:
    @staticmethod
    def create(user, title, content, tags=None):
        note = Note.objects.create(user=user, title=title, content=content)
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
            return Note.objects.get(id=note_id)
        except Note.DoesNotExist:
            return None
        
    
    @staticmethod
    def filter_note(queryFilter):
        return Note.objects.filter(queryFilter)

    @staticmethod
    def update(note, title, content, tags = None):
        note.title = title
        note.body = content
        if tags:
            note.tags.set(tags)
        note.save()
        return note

    @staticmethod
    def delete(note):
        note.delete()

    @staticmethod
    def list_by_owner(user):
        return Note.objects.filter(user=user)

    @staticmethod
    def list_all():
        return Note.objects.all()
