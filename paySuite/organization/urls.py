from django.urls import path , include
from .views import OrganizationViewset
from .views import DepartmentViewset , BanksViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'organization', OrganizationViewset , basename='organization')

departmentRouter = DefaultRouter()
departmentRouter.register(r'department', DepartmentViewset , basename='department')

banksRouter = DefaultRouter()
banksRouter.register(r'banks' , BanksViewset , basename='banks')

urlpatterns = [
    path('api/' , include(router.urls)),
    path('api/' , include(departmentRouter.urls)),
    path('api/' , include(banksRouter.urls))
]
