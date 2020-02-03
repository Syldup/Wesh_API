from rest_framework import serializers
from api.models import *
from unicodedata import normalize, category
import re


class CodePromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodePromo
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        code = re.sub(r"\s+", "", validated_data['code']).upper()
        validated_data['code'] = ''.join((c for c in normalize('NFD', code) if category(c) != 'Mn'))
        return CodePromo.objects.create(**validated_data)


class HistorySerializer(serializers.ModelSerializer):
    code = CodePromoSerializer()

    class Meta:
        model = History
        fields = '__all__'
