from django.db import models

# Create your models here.

class SalaryComponents(models.Model):
    component_name = models.CharField(max_length=50 , null=False)
    component_type = models.CharField(max_length=50 , null=False)
    calculation_method = models.CharField(max_length=100 , null = True)
    default_amount = models.DecimalField(max_digits=10 , decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True , )
    
class SalaryGrades(models.Model):
    grade_name = models.CharField(max_length=100 ,null=False)
    grade_level = models.CharField(max_length=100, null=False)
    
class SalaryGradeComponents(models.Model):
    grade = models.ForeignKey(SalaryGrades , on_delete=models.CASCADE , null=True)
    component = models.ForeignKey(SalaryComponents , on_delete=models.CASCADE , null =True)
    amount =  models.DecimalField(max_digits=100 , decimal_places=2 , null=False)
    frequency = models.CharField(max_length=100 , null=False , default="Monthly")
    is_active = models.CharField(max_length=100 , null=False , default="active")