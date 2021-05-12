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
