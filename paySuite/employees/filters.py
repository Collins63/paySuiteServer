import django_filters
from .models import Employees
from .models import Expenses
from .models import Attendance
from .models import Loans
from .models import Loan_Payments
from .models import Loan_Tops

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

class LoansFilter(django_filters.FilterSet):
    employee = django_filters.NumberFilter(field_name='employee', lookup_expr='exact')

    class Meta:
        model = Loans
        # List the fields that can be filtered via query parameters
        fields = ['employee']
        
class LoanPaymentsFilter(django_filters.FilterSet):
    employee = django_filters.NumberFilter(field_name='employee', lookup_expr='exact')

    class Meta:
        model = Loan_Payments
        # List the fields that can be filtered via query parameters
        fields = ['employee']

class LoanTopsFilter(django_filters.FilterSet):
    employee = django_filters.NumberFilter(field_name='employee', lookup_expr='exact')

    class Meta:
        model = Loan_Tops
        # List the fields that can be filtered via query parameters
        fields = ['employee']