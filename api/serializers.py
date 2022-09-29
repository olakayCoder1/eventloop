from rest_framework import serializers
from account.models import CustomUser 
from .models import *
from rest_framework import status
from account.models import TokenActivation , CustomUser
from multiprocessing import AuthenticationError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str , force_str , smart_bytes , DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode , urlsafe_base64_encode



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'address', 'phone_number' , 'profile_image' ]
    
 


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input-type': 'password'} , write_only= True)
    class Meta:
        model = CustomUser 
        fields = [ 'first_name','last_name',  'email', 'password', 'password2' ]

        extra_kwargs = {
            'password':{'write_only': True},
        }
 

    def save(self):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        user = CustomUser( first_name=first_name, last_name=last_name,  email=email)

        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : 'Email already exist'})

        if len(password) < 8:
            raise serializers.ValidationError({'error': 'password must be at least eight characters'})
        if password != password2 :
            raise serializers.ValidationError({'error': 'password does not match'})

        user.set_password(password)
        user.save()
        return user





class ResetPasswordRequestEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    class Meta:
        fields =  ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=1,max_length=30, write_only=True)
    password2 = serializers.CharField(min_length=1,max_length=30, write_only=True)
    
    class Meta:
        fields = ['password', 'password2']

   

class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


    def save(self):
        request = self.context.get('request')
        old_password = self.validated_data['old_password']
        new_password = self.validated_data['new_password']
        user = CustomUser.objects.get(id=request.user.id)
        if not user.check_password(old_password):
            raise serializers.ValidationError({'error': 'Incorrect password','status': status.HTTP_400_BAD_REQUEST})
        user.set_password(new_password)
        user.save()
        return user
        
        

