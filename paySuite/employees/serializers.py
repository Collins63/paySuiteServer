from rest_framework import serializers
from .models import Employees,Attendance , Expenses
from datetime import date, datetime

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        
    def validate(self, data):
        employee_id = data.get('employee').id
        
        active_check_in_exists = Attendance.objects.filter(
            employee__id=employee_id,
            date=date.today(),
            #check_out__isnull=True  # Find an open session
        ).exists()

        if active_check_in_exists:
            # If an open record is found, raise a validation error
            raise serializers.ValidationError(
                {"detail": "Check-in denied. An active check-in record already exists for this employee today. ⚠️"}
            )
        
        return data
