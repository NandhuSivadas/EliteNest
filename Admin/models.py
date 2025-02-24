from django.db import models


# Create your models here.
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=10)
    admin_email=models.CharField(max_length=10)
    admin_password=models.CharField(max_length=10)


class tbl_category(models.Model):
    category_name=models.CharField(max_length=10)


    