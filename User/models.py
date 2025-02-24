from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.

class tbl_review(models.Model):
    review=models.CharField(max_length=100)

class tbl_cart(models.Model):
    userid=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    cart_qty=models.IntegerField()
    house=models.ForeignKey(tbl_house,on_delete=models.CASCADE)
    cart_status=models.CharField(max_length=10,default=0)

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    house=models.ForeignKey(tbl_house,on_delete=models.CASCADE)
    booking_amount=models.CharField(max_length=50)
    booking_status=models.CharField(max_length=10,default=0)
    payment_status=models.CharField(max_length=10,default=0)