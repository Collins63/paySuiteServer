from django.urls import path , include
from .views import OrganizationViewset
from .views import DepartmentViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'organization', OrganizationViewset , basename='organization')

departmentRouter = DefaultRouter()
departmentRouter.register(r'department', DepartmentViewset , basename='department')

urlpatterns = [
    path('api/' , include(router.urls)),
    path('api/' , include(departmentRouter.urls))
]
