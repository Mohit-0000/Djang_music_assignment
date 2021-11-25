import re
from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , AllowAny
# Create your views here.


class StudentAssignment(APIView):
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)
    def get(self,request):
        print("skjdasdasdasdasd",request.user)
        assignment_object=models.StudentAssignment.objects.all()
        # assignment_object=models.StudentAssignment.objects.filter(student_id=request.user.id)
        serializer=serializers.StudentAssignmentSerializer(assignment_object,many=True).data
        if serializer:
            return Response(serializer,status=status.HTTP_200_OK)
        return Response("NOT FOUND",status=status.HTTP_200_OK)
        
    def post(request):
        serializer=serializers.StudentAssignmentSerializer(student=request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        