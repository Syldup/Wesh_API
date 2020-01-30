from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *


class CodePromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodePromo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
