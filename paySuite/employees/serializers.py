from rest_framework import serializers
from .models import Employees,Attendance , Expenses

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        field = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        field = '__all__'
