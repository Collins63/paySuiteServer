from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeViewset(APIView):
    def get(self, request , id=None):
        if id:
            item = models.Employees.objects.get(id=id)
            serializer = serializers.EmpoyeeSerializer(item)
            return Response({"status": "success" , "data": serializer.data} , status=status.HTTP_200_OK)
        
        items= models.Employees.objects.all()
        serializer = serializers.EmpoyeeSerializer(items, many=True)
        return Response({"status": "success" , "data": serializer.data} , status=status.HTTP_200_OK)
    
    def post(self , request):
        serializer = serializers.EmpoyeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save
            return Response({"status": "success" , "data": serializer.data} , status=status.HTTP_200_OK)
        else:
            return Response({"status": "error" , "data": serializer.data} , status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self , request , id=None):
        item = models.Employees.objects.get(id=id)
        serializer = serializers.EmpoyeeSerializer(item , data = request.data , partial = True)
        if serializer.is_valid():
            serializer.save
            return Response({"status": "success" , "data": serializer.data} , status=status.HTTP_200_OK)
        else:
            return Response({"status": "error" , "data": serializer.data} , status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self , request , id=None):
        item = models.Employees.objects.filter(id=id)
        item.delete()
        return Response({"status": "success" , "data": "Employee deleted"} , status=status.HTTP_200_OK)