from django.urls import path , include
from .views import EmployeeViewset
from rest_framework.routers import DefaultRouter

detail_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

router = DefaultRouter()
router.register(r'employees', EmployeeViewset, basename='employee')

urlpatterns = [
    path('api/', include(router.urls)),
]