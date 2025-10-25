from django.urls import path , include
from .views import EmployeeViewset , AttendanceViewset , ExpenseViewset
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

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/' , include(expenseRouter.urls)),
    path('api/' , include(attendanceRouter.urls))
]