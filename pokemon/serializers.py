from rest_framework import serializers
from .models import Pokemon, Test

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'url', 'title']
