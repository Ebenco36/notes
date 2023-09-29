# Import start
from django.db.models import Q
from rest_framework import generics
from utils.response import ApiResponse 
from notes.serializers import NoteSerializer
from rest_framework import generics, status
from notes.permissions import IsOwnerOrReadOnly
from users.renderers import ResponseJSONRenderer
from rest_framework.permissions import IsAuthenticated
from notes.repositories.note_repository import NoteRepository

# Import ends

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = NoteRepository.list_all()
    renderer_classes = [ResponseJSONRenderer]
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Apply custom permission for object-level permissions

    def perform_create(self, serializer):
        # Set the owner of the post to the currently authenticated user
        serializer.save(user=self.request.user)


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
    
    # The get method handles GET requests to list objects
    def get(self, request, *args, **kwargs):
        # Retrieve the queryset based on the view's queryset attribute
        queryset = self.get_queryset()
        
        # Serialize the queryset data
        serializer = self.get_serializer(queryset, many=True)
        
        # Return the serialized data as the response
        return ApiResponse.success(
            message = "fetch notes successfully", 
            data=serializer.data, 
            status=status.HTTP_200_OK
        )
    

class NoteListCreateViewUP(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [ResponseJSONRenderer]
    queryset = NoteRepository.list_all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Apply custom permission for object-level permissions
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return ApiResponse.success(
            message = "Retrieve notes successfully", 
            data=serializer.data, 
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return ApiResponse.success(
                message = "Updated note successfully", 
                data=serializer.data, 
                status=status.HTTP_201_CREATED
            )
        else:
            return ApiResponse.error(
                message = "Update failed", 
                data=serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return ApiResponse.success(
            message = "Deleted note successfully", 
            status=status.HTTP_204_NO_CONTENT
        )