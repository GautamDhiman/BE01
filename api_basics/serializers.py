from rest_framework import serializers
from .models import Tasks
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tasks
        #fields = ['id', 'title', 'author']
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ['username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user