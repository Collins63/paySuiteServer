from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models
from . import serializers

class ContractorsViewset(viewsets.ModelViewSet):
    queryset = models.Contractors.objects.all()
    serializer_class = serializers.ContractorsSerializer
    
    @action(detail=False, methods=['get'], url_path='count')
    def get_contractors_count(self ,request):
        count = self.queryset.count()
        return Response({'count':count})