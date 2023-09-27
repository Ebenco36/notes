# Import start
from django.db.models import Q
from rest_framework import generics
from utils.response import ApiResponse 
from notes.serializers import NoteSerializer
from notes.permissions import IsOwnerOrReadOnly
from users.renderers import ResponseJSONRenderer
from notes.repositories.tag_repository import TagRepository
from notes.repositories.note_repository import NoteRepository
from rest_framework import generics, permissions, status

# Import ends


class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    renderer_classes = [ResponseJSONRenderer]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query = self.request.query_params.get('q', '').strip() # remove extras
        tag = self.request.query_params.get('tags', []).strip() # remove extras

        # Create a Q object to combine search conditions
        q_objects = Q()

        if query:
            # Add search conditions for title and content fields
            q_objects |= Q(title__icontains=query) | Q(content__icontains=query)

        if tag:
            # Add search condition for tags
            q_objects |= Q(tags__name__icontains=tag)
        if not q_objects.children:
            queryset = NoteRepository.list_all()
        else:
            queryset = NoteRepository.filter_note(q_objects)
            
        return queryset
    
    
    def perform_create(self, serializer):
        title = serializer.validated_data['title']
        content = serializer.validated_data['content']
        tags = serializer.validated_data.get('tags', [])

        
        """
            Create or retrieve tags

            This allow users to create tags while creating a note 
            should in case tag doesn't exist.
        """
        tag_objects = [TagRepository.get_or_create_tag(tag_name) for tag_name in tags]


        note = NoteRepository.create_note(self.request.user, title, content, tag_objects)
        serializer = NoteSerializer(note)
        return ApiResponse.success(
            data=serializer.data, 
            message="Note has been successfully created", 
            status=status.HTTP_201_CREATED
        )

class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    renderer_classes = [ResponseJSONRenderer]
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        return NoteRepository.get_by_id(self.kwargs['pk'])
    

    def update(self, request, *args, **kwargs):
        note = self.get_object()
        serializer = self.get_serializer(note, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return ApiResponse.success(
            data=serializer.data, 
            message="Note has been successfully updated", 
            status=status.HTTP_200_OK
        )

    def delete(self, request, *args, **kwargs):
        note = self.get_object()
        NoteRepository.delete(note)
        return ApiResponse.success(
            data={}, 
            message="Note has been successfully deleted", 
            status=status.HTTP_204_NO_CONTENT
        )