from rest_framework import serializers
from .models import LoginDetails, AppDetails, TaskDetails

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginDetails
        fields = ['username', 'password']

class AppDetailsSerializer(serializers.ModelSerializer):
    icons = serializers.ImageField()
    class Meta:
        model = AppDetails
        fields = ['icons', 'appName', 'appLink', 'category', 'subCategory', 'points']

class TaskDetailsSerializer(serializers.ModelSerializer):
    screenShot = serializers.ImageField()
    class Meta:
        model = TaskDetails
        fields = ['username', 'tasksId', 'points', 'screenShot']