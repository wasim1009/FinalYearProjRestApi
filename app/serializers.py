from rest_framework import serializers
from .models import Lecturer, Room

class LecturerSerializer(serializers.ModelSerializer):
    room = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Lecturer
        fields = ('title','course','profession', 'room', 'module')
        depth = 1
#
# class ModuleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Module
#         fields = ('description', 'module')
#         depth = 1

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        depth = 1
