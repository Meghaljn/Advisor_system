from rest_framework import serializers
from .models import advisors,booking
#from .models import users
from django.contrib.auth.models import User


class advisorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = advisors
        fields = ('name',
                  'photo_url','id','image_file')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username',
                  'email',
                  'password',
                  )


class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ('id','user_id','advisor_id','booking_date_time',)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])

        return user



    # def create(self, validated_data):
    #     username = validated_data["username"]
    #     email = validated_data["email"]
    #     password = validated_data["password"]
    #     #password2 = validated_data["password2"]
    #     if (email and users.objects.filter(email=email).exclude(username=username).exists()):
    #         raise serializers.ValidationError(
    #             {"email": "Email addresses must be unique."})
    #     #if password != password2:
    #         #raise serializers.ValidationError(
    #             #{"password": "The two passwords differ."})
    #     user = users(username=username, email=email)
    #     user.set_password(password)
    #     user.save()
    #     return user