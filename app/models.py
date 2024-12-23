from django.db import models

# Create your models here.
class Dept(models.Model):
    Dept_no=models.IntegerField(primary_key=True)
    Dept_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
class Emp(models.Model):
    Emp_no=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=4)
    comm=models.DecimalField(max_digits=10,decimal_places=4,null=True,blank=True)
    hire_date=models.DateField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True)
    