from django.contrib import admin
from .models import Lecturer

@admin.register(Agencies)
class LecturerAdmin(UserAdmin):
    list_display  = [ '__str__' ]
