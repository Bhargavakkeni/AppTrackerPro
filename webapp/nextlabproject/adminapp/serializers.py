from rest_framework import serializers
from .models import LoginDetails

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginDetails
        fields = ['username', 'password']