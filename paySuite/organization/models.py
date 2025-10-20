from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=200 , null=False)
    address = models.CharField(max_length=300, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    logo = models.ImageField(upload_to='organizationLogos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Department(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=200 , null=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
