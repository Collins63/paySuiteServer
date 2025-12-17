from django.db import models
from employees.models import Employees

class CompanyAssets(models.Model):
    asset_name = models.CharField(max_length=50, null=False)
    asset_id = models.CharField(max_length=10 , null=False)
    description  = models.CharField(max_length=100 , null=False)
    category = models.CharField(max_length=100, null=False)
    asset_value = models.DecimalField(max_digits=100, decimal_places=2 , null=False)
    aquisition_date = models.DateField(null=False)
    status = models.CharField(max_length=100 , null=True , default='Active')
    
class AssetLinks(models.Model):
    asset = models.ForeignKey(CompanyAssets , on_delete=models.CASCADE , null=False)
    employee = models.ForeignKey(Employees , on_delete=models.CASCADE , null= False)
    link_date = models.DateField(auto_now_add=True)
    value_at_link = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    