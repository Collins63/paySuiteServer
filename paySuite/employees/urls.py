from django.urls import path , include
from .views import EmployeeViewset , AttendanceViewset , ExpenseViewset , LoansViewset ,LoanPaymentsViewset , LoanTopsViewset
from rest_framework.routers import DefaultRouter

detail_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

router = DefaultRouter()
router.register(r'employees', EmployeeViewset, basename='employee')

expenseRouter = DefaultRouter()
expenseRouter.register(r'expenses' , ExpenseViewset , basename='expenses')

attendanceRouter = DefaultRouter()
attendanceRouter.register(r'attendance'  , AttendanceViewset , basename='attendance')

loansRouter = DefaultRouter()
loansRouter.register(r'loans'  , LoansViewset , basename='loans')

loanPaymentsRouter = DefaultRouter()
loanPaymentsRouter.register(r'loanPayments'  , LoanPaymentsViewset , basename='loanPayments')

loanTopsRouter = DefaultRouter()
loanTopsRouter.register(r'loanTops'  , LoanTopsViewset , basename='loanTops')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/' , include(expenseRouter.urls)),
    path('api/' , include(attendanceRouter.urls)),
    path('api/' , include(loansRouter.urls)),
    path('api/' , include(loanPaymentsRouter.urls)),
    path('api/' , include(loanTopsRouter.urls))
]