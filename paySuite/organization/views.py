from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models
from . import serializers

class OrganizationViewset(viewsets.ModelViewSet):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    
class BanksViewset(viewsets.ModelViewSet):
    queryset = models.Banks.objects.all()
    serializer_class = serializers.BanksSerializer
    
    @action(detail=False , methods=['get'] , url_path='count')
    def get_bank_count(self, request):
        count = self.queryset.count()
        return Response({'count':count})

# Create your views here.
