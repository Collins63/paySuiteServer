from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUser(AbstractUser):
    # id = models.AutoField(primary_key=True)
    # password = models.CharField(max_length=128)
    # last_login = models.DateTimeField(blank=True, null=True)
    # is_superuser = models.BooleanField()
    # username = models.CharField(unique=True, max_length=150)
    # first_name = models.CharField(max_length=150, blank=True)
    # last_name = models.CharField(max_length=150, blank=True)
    # email = models.EmailField(blank=True)
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField()
    #employee_id = models.IntegerField(null=True)

    class Meta:
        managed = False  # Django will NOT try to create or change this table
        db_table = 'auth_user'

# Create your models here.
