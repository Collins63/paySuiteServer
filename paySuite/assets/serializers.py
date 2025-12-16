from rest_framework import serializers
from .models import CompanyAssets , AssetLinks

class CompanyAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAssets
        fields = '__all__'
        
class AssetLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetLinks
        fields = '__all__'