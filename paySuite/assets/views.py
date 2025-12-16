from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models , serializers

class CompanyAssestViewset(viewsets.ModelViewSet):
    queryset = models.CompanyAssets.objects.all()
    serializer_class = serializers.CompanyAssetsSerializer
    
class AssetLinksViewset(viewsets.ModelViewSet):
    queryset = models.AssetLinks.objects.all()
    serializer_class = serializers.AssetLinksSerializer