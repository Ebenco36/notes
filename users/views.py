from rest_framework import generics, status
from rest_framework.response import Response
from users.serializers import CreateUserSerializer
from users.repositories.user import UserRepository
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class UserListView(generics.ListAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        user_repo = UserRepository()
        return user_repo.get_all_users()
    


class UserCreateView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user_repo = UserRepository()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = user_repo.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_repo = UserRepository()
        return user_repo.get_user_by_id(self.request.user.id)

class UserProfileUpdateView(generics.UpdateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_repo = UserRepository()
        return user_repo.get_user_by_id(self.request.user.id)

    def update(self, request, *args, **kwargs):
        user_repo = UserRepository()
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            user_repo.update_user(instance.id, **serializer.validated_data)
            return Response(serializer.validated_data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(generics.DestroyAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_repo = UserRepository()
        return user_repo.get_user_by_id(self.request.user.id)

    def destroy(self, request, *args, **kwargs):
        user_repo = UserRepository()
        instance = self.get_object()
        user_repo.delete_user(instance.id)
        return Response(status=status.HTTP_204_NO_CONTENT)

