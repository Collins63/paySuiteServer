import django_filters
from .models import Employees
from .models import Expenses
from .models import Attendance

class EmployeeFilter(django_filters.FilterSet):
    # Define a filter field named 'department_id'
    department_id = django_filters.NumberFilter(field_name='department_id', lookup_expr='exact')

    class Meta:
        model = Employees
        # List the fields that can be filtered via query parameters
        fields = ['department_id']
        
class ExpenseFilter(django_filters.FilterSet):
    employee = django_filters.NumberFilter(field_name='employee', lookup_expr='exact')

    class Meta:
        model = Expenses
        # List the fields that can be filtered via query parameters
        fields = ['employee']

class AttendanceFilter(django_filters.FilterSet):
    employee = django_filters.NumberFilter(field_name='employee', lookup_expr='exact')

    class Meta:
        model = Attendance
        # List the fields that can be filtered via query parameters
        fields = ['employee']