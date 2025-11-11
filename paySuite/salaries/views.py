from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class SalaryComponentsViewset(viewsets.ModelViewSet):
    queryset = models.SalaryComponents.objects.all()
    serializer_class = serializers.SalaryComponentsSerializer
    
class SalaryGradesViewset(viewsets.ModelViewSet):
    queryset = models.SalaryGrades.objects.all()
    serializer_class = serializers.SalaryGradesSerializer

class SalaryGradeComponentsViewset(viewsets.ModelViewSet):
    queryset = models.SalaryGradeComponents.objects.all()
    serializer_class = serializers.SalaryGradeComponentsSerializer

# Create your views here.
