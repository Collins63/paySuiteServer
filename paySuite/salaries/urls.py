from django.urls import path , include
from .views import SalaryComponentsViewset , SalaryGradeComponentsViewset ,SalaryGradesViewset
from rest_framework.routers import DefaultRouter

salaryComponentsRouter = DefaultRouter()
salaryComponentsRouter.register(r'salaryComponents', SalaryComponentsViewset , basename='salaryComponents')


salaryGradeCompRouter = DefaultRouter()
salaryGradeCompRouter.register(r'salaryGradeComponents', SalaryGradeComponentsViewset , basename='salaryGradeComponents')

salaryGradesRouter = DefaultRouter()
salaryGradesRouter.register(r'salaryGrades', SalaryGradesViewset, basename='salaryGrades')

urlpatterns = [
    path('api/' ,include(salaryComponentsRouter.urls)),
    path('api/' , include(salaryGradeCompRouter.urls)),
    path('api/' , include(salaryGradesRouter.urls))
]
