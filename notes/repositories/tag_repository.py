from notes.models import Tag

class TagRepository:
    @staticmethod
    def create_tag(name):
        return Tag.objects.create(name=name)

    @staticmethod
    def get_tag_by_id(tag_id):
        try:
            return Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return None
    
    @staticmethod
    def get_tag_by_name(name):
        try:
            return Tag.objects.get(name=name)
        except Tag.DoesNotExist:
            return None

    @staticmethod
    def get_tags_by_names(names):
        return Tag.objects.filter(name__in=names)

    @staticmethod
    def update_tag(tag, name):
        tag.name = name
        tag.save()

    @staticmethod
    def delete_tag(tag):
        tag.delete()


    @staticmethod
    def get_or_create_tag(name):
        tag = Tag.objects.get_or_create(name=name)
        return tag
