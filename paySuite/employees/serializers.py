from rest_framework import serializers
from .models import Employees

class EmpoyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '_all_'