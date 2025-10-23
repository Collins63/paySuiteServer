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
    address = models.CharField(max_length=250, null=True)
    country = models.CharField(max_length=100 , default='Zimbabwe')
    province = models.CharField(max_length=100 ,null=True)
    nationality = models.CharField(max_length=100, default='Zimbabwean')
    profile_image = models.ImageField(
        upload_to='profiles/', 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True , )

# Create your models here.
class Expenses(models.Model):
    employee=models.ForeignKey(Employees, on_delete=models.CASCADE,null=True)
    description=models.TextField(default="",null=True)
    amount=models.DecimalField(null=True,max_digits=12, decimal_places=5)
    category=models.TextField(default="",null=True)
    expense=models.DateField(default="",null=True)
    approved=models.BooleanField(default=False)


class Attendance(models.Model):
    employee=models.ForeignKey(Employees, on_delete=models.CASCADE,null=True),
    employee_name=models.CharField(max_length=200,default="",null=True)
    date=models.DateField(default="",null=False)
    check_in=models.TimeField(default="",null=False)
    check_out=models.TimeField(default="",null=True)
    status=models.CharField(max_length=100,default="Present",null=False)
    
