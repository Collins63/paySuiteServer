from django.db import models

# Create your models here.
class Contractors(models.Model):
    company_name = models.CharField(max_length=100 , null=False)
    contact_person = models.CharField(max_length=100 , null=False)
    contact_personPhone = models.CharField(max_length=20 , null=False)
    email = models.EmailField(max_length=100 , null=False)
    project = models.CharField(max_length=100 , null=True)
    address = models.CharField(max_length=100 , null=False)
    country = models.CharField(max_length=100 , null=False , default="Zimbabwe")
    department_id = models.CharField(max_length=10 , null=False)
    hire_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True , )