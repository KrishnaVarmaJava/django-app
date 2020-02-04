from rest_framework import serializers
from .models import User

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'firstName', 'lastName')
