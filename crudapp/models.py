from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Student(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	adm_no = models.IntegerField()
	passport = models.FileField()

	def get_absolute_url(self):
		return reverse('crudapp:index')

	def __str__(self):
		return self.firstname


