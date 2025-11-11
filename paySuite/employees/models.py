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

class Expenses(models.Model):
    employee=models.ForeignKey(Employees, on_delete=models.CASCADE,null=True)
    description=models.TextField(default="",null=True)
    amount=models.DecimalField(null=True,max_digits=12, decimal_places=5)
    category=models.TextField(default="",null=True)
    expense=models.DateField(default="",null=True)
    approved=models.BooleanField(default=False)


class Attendance(models.Model):
    employee=models.ForeignKey(Employees, on_delete=models.CASCADE,null=True)
    employee_name=models.CharField(max_length=200,default="",null=True)
    date=models.DateField(auto_now_add=True)
    check_in=models.TimeField(auto_now_add= True)
    check_out=models.TimeField(null=True)
    status=models.CharField(max_length=100,default="Present",null=False)
    hours_worked = models.CharField(max_length=10 , default=0)

class Loans(models.Model):
    employee = models.ForeignKey(Employees , on_delete=models.CASCADE , null=True)
    employee_name = models.CharField(max_length=200 , null=False)
    principal = models.CharField(max_length=200 , null=False)
    interest_rate = models.DecimalField(max_digits=100 , null=False , default=1 ,decimal_places=4)
    total_amount = models.DecimalField(max_digits=100 , null=False , decimal_places=4)
    balance = models.DecimalField(max_digits=100 , null=False , decimal_places=4)
    months = models.CharField(max_length=200 , null=False, default='1')
    start_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100 , default="Active")
    payment_period = models.CharField(max_length=100 , default="Monthly")
    
class Loan_Payments(models.Model):
    employee = models.ForeignKey(Employees , on_delete=models.CASCADE , null=True)
    loan = models.ForeignKey(Loans , on_delete=models.CASCADE , null=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    balance_on_date = models.DecimalField(max_digits=100 , decimal_places=2)
    
class Loan_Tops(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE , null=False)
    loan = models.ForeignKey(Loans , on_delete=models.CASCADE , null = False)
    amount = models.DecimalField(max_digits=100 , decimal_places=2 , null=False)
    date = models.DateField(auto_now_add=True)
    balance_on_date = models.DecimalField(max_digits=100 , decimal_places=2)
    
