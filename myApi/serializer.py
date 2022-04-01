from xml.parsers.expat import model
from attr import fields
from rest_framework import serializers
from todo.models import todoDataSet

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoDataSet
        fields = '__all__'