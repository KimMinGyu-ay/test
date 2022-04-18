from django.db import models

# Create your models here.

class user_list(models.Model):
    user_name =models.CharField(max_length=5, verbose_name="사용자")
    gender = models.CharField(max_length=5, verbose_name="성별")
    age=models.IntegerField( verbose_name="나이")
    user_id = models.CharField(max_length=10, verbose_name="ID")
    password = models.CharField(max_length=13,verbose_name="PW")
    e_mail = models.CharField(max_length=20,verbose_name="이메일")
    class Meta:
        db_table = "user_list"


        
# userId, 
# email,
# password, 
# name, 
# gender,

# isVerified
# updatedAt, 
# createdAt
