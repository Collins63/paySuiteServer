from rest_framework import serializers
from .models import Contractors

class ContractorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractors
        fields = '__all__'