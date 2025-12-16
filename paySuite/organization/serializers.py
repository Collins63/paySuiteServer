from rest_framework import serializers
from .models import Organization , Department , Banks

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = '__all__'