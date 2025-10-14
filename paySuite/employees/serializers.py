from rest_framework import serializers
from .models import Employees,Expenses

class EmpoyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '_all_'
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        field = 'all'