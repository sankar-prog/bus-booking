from django.db import models


from django.utils import timezone

# Create your models here.
class customers(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=200)
    phno=models.IntegerField()
    password=models.CharField(max_length=200)
    
class bus(models.Model):
    service_no=models.IntegerField(primary_key=True)
    start=models.CharField(max_length=200)
    end=models.CharField(max_length=200)
    seats_available=models.IntegerField()
    price=models.IntegerField()
    
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # tuple('',)
    # list['']
    
    
class booking_history(models.Model):
    # ticket_no=models.IntegerField(primary_key=True)
    ticket_no=models.CharField(primary_key=True,max_length=200)
    # reference the table
    
    # dontgive ondelete error throw
    # it refential constraint in sql
    customer_id=models.ForeignKey(customers,on_delete=models.RESTRICT)
    service_no=models.ForeignKey(bus,on_delete=models.RESTRICT)
    no_of_seats=models.IntegerField()
    amount=models.IntegerField()
    
    
    
    travelling_date=models.DateField(default=timezone.now)
    
    
    
    
    
    
    
    