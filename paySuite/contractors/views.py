from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class ContractorsViewset(viewsets.ModelViewSet):
    queryset = models.Contractors.objects.all()
    serializer_class = serializers.ContractorsSerializer