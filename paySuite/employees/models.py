from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dob = models.CharField(max_length=100 , default='01/01/1960')
    hire_date = models.CharField(max_length=100)
    organization_id = models.CharField(max_length=100)
    department_id = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

# Create your models here.
class Expenses(models.Model):
    employee=models.ForeignKey(Employees, on_delete=models.CASCADE,null=True)
    description=models.TextField(default="",null=True)
    amount=models.DecimalField(null=True,max_digits=12, decimal_places=5)
    category=models.TextField(default="",null=True)
    expense=models.DateField(default="",null=True)
    approved=models.BooleanField(default=False)

class Loans(models.Model):
    employee=models.ForeignKey(Employees, on_delete=models.CASCADE,null=True)
    principal=models.TextField(null=True)
    interest_rate=models.DecimalField(null=True,max_digits=12, decimal_places=5)
    total_amount=models.DecimalField(null=True,max_digits=12, decimal_places=5)
    balance=models.DecimalField(null=True,max_digits=12, decimal_places=5)
    start_date=models.DateTimeField(null=True)
    status=models.BooleanField(default=False)