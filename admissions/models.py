from django.db import models


class AdmissionForm(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	id_number = models.CharField(max_length=13)

	address = models.CharField(max_length=100)
	suburb = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	code = models.CharField(max_length=10)

	parent_firstName = models.CharField(max_length=100)
	parent_lastName = models.CharField(max_length=100)
	parent_idNumber = models.CharField(max_length=100)
	parent_cellNumber = models.CharField(max_length=10)
	parent_emailAddress = models.EmailField(max_length=100)

	parent_address = models.CharField(max_length=100)




	def __str__(self):
		return f"{self.first_name} {self.last_name}, {self.id_number}"

