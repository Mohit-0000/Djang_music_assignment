# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class StudentAssignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100,blank=True)
    description=models.TextField(max_length=5000,blank=True)
    music_genre=models.CharField(max_length=20, blank=True)
    DailyPracticeTime=models.TimeField(blank=True)
    Days=models.PositiveIntegerField(blank=True)
    
    def __str__(self):
            return str(self.pk)
