from django.urls import path
from .views import EmployeeViewset

urlpatterns = [
    path('api/employees/', EmployeeViewset.as_view()),
    path('api/employees/<int:id>' , EmployeeViewset.as_view())
]
