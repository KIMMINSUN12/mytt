from rest_framework import serializers
from .models import Info, Info2

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id', 'schoolname', 'semester', 'credit')

class Info2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Info2
        fields = ('id', 'major', 'minor', 'elective','max_lecture','no_class_day')