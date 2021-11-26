from rest_framework import serializers
from . import models



class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model =models.StudentAssignment
        fields ='__all__'