from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


class EmployeeViewset(viewsets.ModelViewSet):
        
    queryset = models.Employees.objects.all()
    serializer_class = serializers.EmployeeSerializer
    # @csrf_exempt
    # def get(self, request , id=None):
    #     if id:
    #         item = models.Employees.objects.get(id=id)
    #         serializer = serializers.EmployeeSerializer(item)
    #         return Response({"status": "success" , "data": serializer.data} , status=status.HTTP_200_OK)
        
    #     items= models.Employees.objects.all()
    #     serializer = serializers.EmployeeSerializer(items, many=True)
    #     return Response({"status": "success" , "data": serializer.data} , status=status.HTTP_200_OK)
    
    # @csrf_exempt
    # def create(self, request):
    #     serializer = serializers.EmployeeSerializer(data=request.data)
        
    #     # Check if data is valid
    #     if serializer.is_valid():
            
    #         # ❌ FIX 1: You must call .save() with parentheses: serializer.save()
    #         serializer.save()
            
    #         # ❌ FIX 2: HTTP 201 (Created) is the standard response for successful POST/creation
    #         return Response(
    #             {"status": "success", "data": serializer.data}, 
    #             status=status.HTTP_201_CREATED # Use 201 for creation
    #         )
        
    #     # If validation fails
    #     else:
    #         # ✅ FIX 3: Return the specific validation errors, not the raw data
    #         return Response(
    #             {"status": "error", "message": serializer.errors}, # Return serializer.errors for detail
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    
    # @csrf_exempt
    # def patch(self , request , id=None):
    #     item = models.Employees.objects.get(id=id)
    #     serializer = serializers.EmployeeSerializer(item , data = request.data , partial = True)
    #     if serializer.is_valid():
    #         serializer.save
    #         return Response({"status": "success" , "data": serializer.data} , status=status.HTTP_200_OK)
    #     else:
    #         return Response({"status": "error" , "data": serializer.data} , status=status.HTTP_400_BAD_REQUEST)
    
    # @csrf_exempt    
    # def delete(self , request , id=None):
    #     item = models.Employees.objects.filter(id=id)
    #     item.delete()
    #         return Response({"status": "success" , "data": "Employee deleted"} , status=status.HTTP_200_OK)