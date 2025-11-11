from django.urls import path , include
from .views import ContractorsViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'contractors' , ContractorsViewset , basename='contractors')

urlpatterns = [
    path('api/' , include(router.urls))
]
