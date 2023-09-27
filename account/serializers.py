from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

"""
    Note that serializer to create a new user already exist with the Users App
"""
class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        token = None
        if email and password:
            token = super().validate(data)
        else:
            raise serializers.ValidationError({
                'message': 'Must include "email" and "password".'
            })
        
        data['token'] = token
        return data

