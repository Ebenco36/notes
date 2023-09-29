from django.contrib import admin
from notes.models import Note
# Register your models here.

admin.site.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "tag_list"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())