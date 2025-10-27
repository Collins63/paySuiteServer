from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from . import filters
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from datetime import date, datetime


class EmployeeViewset(viewsets.ModelViewSet):
        
    queryset = models.Employees.objects.all()
    serializer_class = serializers.EmployeeSerializer
    
    #filters
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = filters.EmployeeFilter
    
    search_fields = ['^first_name' , '^last_name' , '^email']
    

class ExpenseViewset(viewsets.ModelViewSet):
    queryset = models.Expenses.objects.all()
    serializer_class = serializers.ExpenseSerializer
    
    #filters
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = filters.ExpenseFilter
    
class AttendanceViewset(viewsets.ModelViewSet):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer
    
    #filters
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = filters.AttendanceFilter
    
    search_fields = ['^employee_name']
    
    # ----------------------------------------------------------------------
    # Custom Action for Check-Out (PATCH /api/attendance/checkout/{employee_id}/)
    # ----------------------------------------------------------------------
    
    @action(detail=False ,methods=['patch'] ,url_path=r'checkout/(?P<employee_id>\d+)')
    def checkout(self, request , employee_id = None):
        try:
            attendance_record = self.get_queryset().get(
                employee__id = employee_id,
                date = date.today(),
                check_out__isnull=True
            )
        except models.Attendance.DoesNotExist:
            already_checked_out = self.get_queryset().filter(
                employee__id=employee_id,
                date=date.today(),
                check_out__isnull=False # Look for a record where check_out is filled
            ).exists()
            
            if already_checked_out:
                # Case (b): Already checked out
                return Response(
                    {"detail": "Check-out denied. This employee has already checked out today. 🚫"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                # Case (a): Never checked in
                return Response(
                    {"detail": "Check-out denied. No check-in record found for this employee today. ❌"},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        
        check_out_dt = datetime.now()
        attendance_record.check_out = check_out_dt.time()
        check_in_dt = datetime.combine(attendance_record.date, attendance_record.check_in)
        time_diff = check_out_dt - check_in_dt
        
        total_seconds = time_diff.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60) 
        
        attendance_record.hours_worked = f"{hours:02d}h {minutes:02d}m" 

        attendance_record.save()
        
        return Response(
            {"status": "Check-out recorded successfully", "hours_worked": attendance_record.hours_worked},
            status=status.HTTP_200_OK
        )