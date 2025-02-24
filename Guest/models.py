from django.db import models
from Admin.models import *

# Create your models here.

class tbl_user(models.Model):
    user_name=models.CharField(max_length=20)
    user_contact=models.CharField(max_length=20)
    user_email=models.EmailField()
    user_gender=models.CharField(max_length=20)
    user_address=models.TextField()
    user_photo=models.FileField(upload_to='UserDocs/')
    user_proof=models.FileField(upload_to='UserDocs/')
    user_password=models.CharField(max_length=20)
    user_status=models.IntegerField(default=0)
    
class tbl_owner(models.Model):
    owner_name = models.CharField(max_length=20)
    owner_contact = models.CharField(max_length=20)
    owner_email = models.EmailField()
    owner_gender = models.CharField(max_length=20)
    owner_address = models.TextField()
    owner_photo = models.FileField(upload_to='UserDocs/')
    owner_proof = models.FileField(upload_to='UserDocs/')
    owner_password = models.CharField(max_length=20)
    owner_status = models.IntegerField(default=0)
    
class tbl_house(models.Model):
    house_title=models.CharField(max_length=10)
    house_description=models.CharField(max_length=100)
    house_category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    house_price=models.IntegerField()
    house_image=models.FileField(upload_to='HouseDocs/')
    house_location=models.CharField(max_length=50)
    house_status=models.IntegerField(default=0)
    owner=models.ForeignKey(tbl_owner,on_delete=models.SET_NULL,null=True)
    admin = models.ForeignKey(tbl_admin, on_delete=models.SET_NULL, null=True)