import random
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Send verification email
        send_verification_email(user)
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user and user.is_active:
                if user.verify:
                    token = RefreshToken.for_user(user)
                    return {
                        'email': user.email,
                        'token': str(token.access_token)
                    }
                else:
                    raise serializers.ValidationError("Email not verified")
            else:
                raise serializers.ValidationError("Invalid credentials or account not activated")
        else:
            raise serializers.ValidationError("Both email and password are required.")

def send_verification_email(user):
    user.verify = random.randint(10000, 99999)
    user.save()

    subject = 'Verify your email'
    message = f'Hi {user.email}\n\n code: {user.verify}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)