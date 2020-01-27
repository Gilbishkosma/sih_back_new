from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class Profile(models.Model):
	name = models.CharField(max_length=100)
	designation = models.CharField(max_length=100)
	gender = models.CharField(max_length=100,choices=(('male','male'),('female','female'),('transgender','transgender')))
	age = models.IntegerField()
	phone_no = PhoneNumberField(null=True,blank=True)
	email = models.EmailField(max_length=200,null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name



class AccessLog(models.Model):
	profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="access_log")
	entry_time = models.DateTimeField(auto_now_add=True)
	exit_time = models.DateTimeField(null=True,blank=True)


class Photos(models.Model):
	profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="photo")
	photo = models.ImageField(upload_to="img")