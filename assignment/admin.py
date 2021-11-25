from django.contrib import admin
from . import models
# Register your models here.

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("id","student","title","music_genre","description")

admin.site.register(models.StudentAssignment,AssignmentAdmin)