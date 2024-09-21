from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password



from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']  # Adjust fields as needed


# Getting the custom user model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # Adding fields for password validation
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm', 'bio', 'profile_picture')

    # Custom validation for password match
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    # Overriding the create method to handle password hashing
    def create(self, validated_data):
        # Remove password_confirm from validated_data as it's not part of the User model
        validated_data.pop('password_confirm')

        # Creating the user using the create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),  # Optional field
            profile_picture=validated_data.get('profile_picture', None)  # Optional field
        )

        return user
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'following', 'followers']
        depth = 1  # Show detailed follow information

