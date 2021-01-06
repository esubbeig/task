from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length=500)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class DataResult(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)