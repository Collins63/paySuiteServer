from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from . import filters
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class EmployeeViewset(viewsets.ModelViewSet):
        
    queryset = models.Employees.objects.all()
    serializer_class = serializers.EmployeeSerializer
    
    #filters
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = filters.EmployeeFilter
    
    search_fields = ['^first_name' , '^last_name' , '^email']
    

class ExpenseViewset(viewsets.ModelViewSet):
    queryset = models.Expenses.objects.all()
    serializer_class = serializers.ExpenseSerializer
    
    #filters
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = filters.ExpenseFilter
    
class AttendanceViewset(viewsets.ModelViewSet):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer
    
    #filters
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = filters.AttendanceFilter
    
    search_fields = ['^employee_name']