from django.db import models
# Create your models here.
class Bussiness(models.Model):
    Bname=models.CharField(max_length = 64)

class Host(models.Model):
    hid=models.AutoField(primary_key = True)
    Hname=models.CharField(max_length = 32,db_index = True)
    ip=models.GenericIPAddressField(db_index = True)
    port=models.IntegerField()
    f=models.ForeignKey(to='Bussiness',to_field = 'id',on_delete=models.CASCADE)


class UserInfo(models.Model):
    username=models.CharField(max_length = 32)
    password=models.CharField(max_length = 64)
    email=models.CharField(max_length = 64,default = 'root@163.com')
    addrese=models.CharField(max_length = 64,default = 'xian')

