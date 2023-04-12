from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from db.users.models import User


class UserSignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({
                'email': 'User with this email already exists'
            })

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")

        return attrs

    def create(self, validated_data):
        User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return validated_data


class UserAuthSerialzier(TokenObtainPairSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'last_login')
