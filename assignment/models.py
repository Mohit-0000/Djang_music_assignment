# -*- coding: utf-8 -*-

from django.db import models

class StudentAssignment(models.Model):
    title=models.CharField(max_length=100,blank=True)
    description=models.TextField(max_length=5000,null=True, blank=True)
    music_genre=models.CharField(max_length=20, blank=True,null=True)
    DailyPracticeTime=models.TimeField(blank=True,null=True)
    Days=models.PositiveIntegerField(blank=True,null=True)
    DaysPracticed=models.PositiveIntegerField(blank=True,null=True)
    def __str__(self):
            return str(self.title)
