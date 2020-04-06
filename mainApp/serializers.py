from rest_framework import serializers
from .models import UserDetail, PlotHistory
from django.contrib.auth.models import User

class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'username', 'date_joined', 'last_login', 'email')

class UserDetailsSerializer(serializers.ModelSerializer):
    user=serializers.CharField(source="user.username")
    other_details=UserSerilizer(source="user")

    class Meta:
        model=UserDetail  # what module you are going to serialize
        fields= '__all__'

class PlotHistorySerializer(serializers.ModelSerializer):
    user=serializers.CharField(source="user.username")

    class Meta:
        model=PlotHistory
        fields=('user', 'id', 'points', 'created_on')
