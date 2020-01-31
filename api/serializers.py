from rest_framework import serializers
from api.models import *


class CodePromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodePromo
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
