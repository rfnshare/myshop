from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from users.models import CustomUser

# Get the CustomUser model
User = get_user_model()

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=100, required=True)
    profile_pic = serializers.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'phone_number', 'first_name', 'last_name', 'profile_pic')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Handle password and profile pic separately
        password = validated_data.pop('password', None)
        user = CustomUser.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()

        # If a profile pic is provided, save it
        if 'profile_pic' in validated_data:
            user.profile_pic = validated_data['profile_pic']
            user.save()

        return user

class CustomUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number','first_name', 'last_name', 'profile_pic', 'is_staff']

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'profile_pic')
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate_email(self, value):
        """Check if the email is unique."""
        user = self.context['request'].user
        if CustomUser.objects.exclude(id=user.id).filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

class AdminCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # Only an admin can create another admin
        request = self.context.get('request')
        if not request.user.is_staff:
            raise serializers.ValidationError("You do not have permission to create an admin user.")
        return data

    def create(self, validated_data):
        # Create the user as an admin (is_staff=True)
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'is_active']

