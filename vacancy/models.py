from django.db import models


class Vacancy(models.Model):
	title = models.CharField(max_length=100)
	opening_date = models.DateField()
	closing_date = models.DateField()
	link = models.URLField()
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.title}"
