# Start of Import
from utils.response import ApiResponse 
from rest_framework.views import APIView
from rest_framework import generics, status
from account.serializers import LoginSerializer
# from rest_framework.authtoken.models import Token
from users.serializers import CreateUserSerializer
from users.repositories.user import UserRepository
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.serializers import CreateUserSerializer, UserSerializer

# End of Import


"""
    We are open to several options to generate user token
    *** Django REST Framework Token Authentication
    Django's Built-in Token Authentication
    JWT (JSON Web Tokens) TokenObtainPairView vis simplejwt
    and others
"""
class UserLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            tokens = serializer.validated_data['token']

            # Check if the token response contains 'access' and 'refresh' keys
            if 'access' in tokens and 'refresh' in tokens:

                return ApiResponse.success(tokens)
            else:
                return ApiResponse.error(
                    data={'error': 'Token not found'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
        else:
            return ApiResponse.error(
                data=serializer.errors, 
                status=status.HTTP_401_UNAUTHORIZED
            )

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)  # Serialize the user data
        return ApiResponse.success(
            data=serializer.data, 
            message="User profile fetch successfully", 
            status=status.HTTP_200_OK
        )
    

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        user_repo = UserRepository()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = user_repo.create_user(**serializer.validated_data)

            if user:
                return ApiResponse.success(
                    data=serializer.validated_data, 
                    message="User profile created successfully", 
                    status=status.HTTP_201_CREATED
                )
            else:
                return ApiResponse.error(
                    data={"error": "User with this email already exists."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return ApiResponse.error(
                data=serializer.errors, 
                status=status.HTTP_401_UNAUTHORIZED
            )
                
            

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()  # Add the refresh token to the blacklist
            return ApiResponse.success(
                data={"message": "logged out successfully"},
                status=status.HTTP_205_RESET_CONTENT
            )
        
        except Exception as e:
            return ApiResponse.error(
                data=str(e), 
                status=status.HTTP_400_BAD_REQUEST
            )