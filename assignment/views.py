from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView


'''
API view for List assignment and create assignment
'''
class StudentAssignment(APIView):
    def get(self,request):
        assignment_object=models.StudentAssignment.objects.all()
        serializer=serializers.StudentAssignmentSerializer(assignment_object,many=True).data
        if serializer:
            return Response(serializer,status=status.HTTP_200_OK)
        return Response("NOT FOUND",status=status.HTTP_200_OK)
        
    def post(self,request):
        serializer=serializers.StudentAssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        