from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserRegistrationSerializer, CustomUserLoginSerializer, UserProfileSerializer, \
    UpdateProfileSerializer


class RegisterUserView(APIView):
    """
    Class-based view for user registration.
    """

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User created successfully",
                "user": {
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone_number": user.phone_number,
                    "profile_pic": user.profile_pic.url if user.profile_pic else None
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


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutUserView(APIView):
    """
    Class-based view for user logout.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Get the refresh token from the request
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"detail": "Refresh token is required for logout."}, status=status.HTTP_400_BAD_REQUEST)

            # Blacklist the refresh token to invalidate it
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserProfileSerializer(user)

        # Check if user has a profile picture and add the URL to the response data
        if user.profile_pic:
            # Generate the full URL to the profile picture
            profile_pic_url = request.build_absolute_uri(user.profile_pic.url)
            # Add the URL to the serialized data
            data = serializer.data
            data['profile_pic_url'] = profile_pic_url
        else:
            data = serializer.data
            data['profile_pic_url'] = None  # If no profile pic, add None

        return Response(data, status=200)


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = UpdateProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Profile updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

