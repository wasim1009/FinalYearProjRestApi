from django.contrib import admin
from .models import Lecturer, Room

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display  = [ '__str__' ]

# @admin.register(Module)
# class ModuleAdmin(admin.ModelAdmin):
#     list_display  = [ '__str__' ]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display  = [ '__str__' ]

