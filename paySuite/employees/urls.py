from django.urls import path
from .views import EmployeeViewset

detail_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

urlpatterns = [
    # 1. List (GET) and Create (POST) endpoint
    path('api/employees/', EmployeeViewset.as_view({'get': 'list', 'post': 'create'})),
    
    # 2. Detail endpoints (Retrieve, Update, Destroy)
    path('api/employees/<int:pk>/' , EmployeeViewset.as_view(detail_actions)),
    
    # 3. ❌ REMOVE the path('api/employees/post' ... ) line as it is now redundant.
]