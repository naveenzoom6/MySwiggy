from django.db import models
from s_admin.models import AreaModel
from s_admin.models import RestaurantTypeModel


class RestaurantModel(models.Model):
    restro_id = models.AutoField(primary_key=True)
    restro_name = models.CharField(unique=True,max_length=30)
    restro_contact = models.IntegerField(unique=True)
    restro_email = models.EmailField(max_length=100,unique=True)
    restro_area = models.ForeignKey(AreaModel,on_delete=models.CASCADE)
    restro_type = models.ForeignKey(RestaurantTypeModel,on_delete=models.CASCADE)
    restro_password = models.CharField(max_length=30)
    restro_otp = models.IntegerField()
    restro_status = models.CharField(max_length=30,default=False)