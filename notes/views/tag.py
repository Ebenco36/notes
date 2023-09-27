from notes.models import Tag
from utils.response import ApiResponse
from notes.serializers import TagSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from notes.permissions import IsOwnerOrReadOnly
from users.renderers import ResponseJSONRenderer
from notes.repositories.tag_repository import TagRepository
from rest_framework.permissions import IsAuthenticated


class TagListCreateView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    renderer_classes = [ResponseJSONRenderer]

    def get_queryset(self):
        return TagRepository.get_all_tags()

    def perform_create(self, serializer):
        tag_name = serializer.validated_data['name']
        TagRepository.get_or_create_tag(tag_name)
        serializer.save()
        return ApiResponse.success(
            data=serializer.data, 
            message="Tag has been successfully created", 
            status=status.HTTP_201_CREATED
        )

class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    renderer_classes = [ResponseJSONRenderer]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        tag_id = self.kwargs['pk']
        return TagRepository.get_tag_by_id(tag_id) 

    def update(self, request, *args, **kwargs):
        tag = self.get_object()
        serializer = self.get_serializer(tag, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        tag_name = serializer.validated_data['name']
        TagRepository.update_tag(tag, tag_name)
        serializer.save()
        return ApiResponse.success(
            data=serializer.data, 
            message="Tag has been successfully updated", 
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        tag = self.get_object()
        TagRepository.delete_tag(tag)
        return ApiResponse.success(
            data={}, 
            message="Tag has been successfully deleted", 
            status=status.HTTP_204_NO_CONTENT
        )
