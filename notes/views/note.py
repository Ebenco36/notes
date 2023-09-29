# Import start
from django.db.models import Q
from rest_framework import generics
from utils.response import ApiResponse 
from rest_framework import generics, status
from notes.permissions import IsOwnerOrReadOnly
from notes.permissions import IsOwnerOrReadOnly
from users.renderers import ResponseJSONRenderer
from notes.repositories.note_repository import NoteRepository
from notes.serializers import NoteSerializer, CreateNoteSerializer

from rest_framework.permissions import IsAuthenticated

# Import ends


class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    renderer_classes = [ResponseJSONRenderer]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateNoteSerializer
        return NoteSerializer
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '').strip() # remove extras
        tag = self.request.query_params.get('tag', "") # remove extras

        # Create a Q object to combine search conditions
        q_objects = Q()

        if query:
            # Add search conditions for title and content fields
            q_objects |= Q(title__icontains=query) | Q(body__icontains=query)

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
        body = serializer.validated_data['body']
        tags = serializer.validated_data.get('tags', [])

        # create record via our repository
        NoteRepository.create(
            user=self.request.user, 
            title = title, 
            body = body,
            tags = tags,
        )
        # generate response
        return ApiResponse.success(
            data=serializer.data, 
            message="Note has been successfully created", 
            status=status.HTTP_201_CREATED
        )


"""
    Handle GET, UPDATE, DELETE Requests
"""
class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    renderer_classes = [ResponseJSONRenderer]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return NoteRepository.get_note_by_id(self.kwargs['pk'])

    def update(self, request, *args, **kwargs):
        note = self.get_object()
        serializer = self.get_serializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            body = serializer.validated_data['body']
            tags = serializer.validated_data.get('tags', [])
            NoteRepository.update(note=note, title=title, body=body, tags=tags)
            return ApiResponse.success(
                data=serializer.data, 
                message="Note has been successfully updated", 
                status=status.HTTP_200_OK
            )
        else:
            return ApiResponse.error(
                data={"message": "Error has occured"}, 
                message="Could not update note", 
                status=status.HTTP_400_BAD_REQUEST
            )



    def delete(self, request, *args, **kwargs):
        note = self.get_object()
        NoteRepository.delete(note)
        return ApiResponse.success(
            data={}, 
            message="Note has been successfully deleted", 
            status=status.HTTP_204_NO_CONTENT
        )