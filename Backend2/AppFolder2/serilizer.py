from rest_framework import serializers
from .models import User2

class UserSterializer(serializers.ModelSerializer):
    class Meta:
        model = User2
        fields = ['name','email']