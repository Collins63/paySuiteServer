from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class OrganizationViewset(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


# Create your views here.
