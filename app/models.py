from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.db import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class Lecturer(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    course = models.CharField(max_length=100, blank=True, default='')
    profession = models.CharField(max_length=100, blank=True, default='')
    module = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=900, blank=True, default='')

    def __str__(self):
        return "%s" % (self.title)

#
# class Module(models.Model):
#     module = models.CharField(max_length=100, blank=True, default='')
#     description = models.CharField(max_length=900, blank=True, default='')
#     lecturer = models.ForeignKey(Lecturer, on_delete = models.CASCADE, related_name='module')
#
#     def __str__(self):
#         return "%s : %s" % (self.module, self.description)
#
#     def __unicode__(self):
#         return '%s : %s' % (self.module, self.description)

class Room(models.Model):
    room_number = models.CharField(max_length=100, blank=True, default='')
    floor_level = models.IntegerField(blank=True, default=0)
    lecturer = models.ForeignKey(Lecturer, on_delete = models.CASCADE, related_name='room')

    def __str__(self):
        return "%s : %i" % (self.room_number, self.floor_level)

    def __unicode__(self):
        return '%s : %i' % (self.room_number, self.floor_level)
