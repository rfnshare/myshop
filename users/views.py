from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserRegistrationSerializer, CustomUserLoginSerializer


class RegisterUserView(APIView):
    """
    Class-based view for user registration.
    """

    def post(self, request, *args, **kwargs):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User created successfully",
                "user": {
                    "username": user.username,
                    "email": user.email
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    """
    Class-based view for user login.
    """

    def post(self, request, *args, **kwargs):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Create a RefreshToken for the user
                refresh = RefreshToken.for_user(user)

                # Access the access_token from the RefreshToken instance
                access_token = str(refresh.access_token)

                return Response({
                    'message': 'Login successful',
                    'access': access_token,
                    'refresh': str(refresh),
                }, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
