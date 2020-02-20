from django.db import models
from django.conf import settings


# Create your models here.
class bios(models.Model):

	 username = models.CharField(max_length=50)
	 phone_no = models.CharField(max_length=10, unique = True)