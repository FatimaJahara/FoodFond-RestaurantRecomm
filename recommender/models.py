from django.db import models

class Recommend(models.Model):
	userpreference = models.CharField(max_length=200)

	def __str__(self):
		return self.userpreference
		

