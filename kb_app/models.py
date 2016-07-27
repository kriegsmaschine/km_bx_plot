from django.db import models

class Patient(models.Model):
	pt_id		 = models.CharField(max_length=200)

	def __str__(self):
		return self.pt_id

class Patient_Data(models.Model):
	VITAL_STATUS_CHOICE = (
							('A', 'Alive'),
						   	('D', 'Dead')
						  )

	lastContact  = models.FloatField(default = 0)
	exp_brca1    = models.FloatField(default = 0)
	exp_usp1     = models.FloatField(default = 0)
	vital_status = models.CharField(max_length=1, 
									choices = VITAL_STATUS_CHOICE,
									default = 'A')
	patient      = models.ForeignKey(Patient)

	class Meta:
		verbose_name_plural = 'Patient Data'

	def __str__(self):
		return str(self.patient)
