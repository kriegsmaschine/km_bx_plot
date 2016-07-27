#script to load .csv data into database
import sys, os, csv, django

csv_filepathname = "F:/python/km_bx_plot/test_data.csv"
project_path     = "F:\python\km_bx_plot"

sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = "km_bx_plot.settings"
django.setup()

from kb_app.models import Patient, Patient_Data


dataReader = csv.reader(open(csv_filepathname), delimiter = ',', quotechar = '"')

tpatient = None
header = dataReader.__next__()
for row in dataReader:
	if tpatient != row[0]:
		tpatient = row[0]
		patient  = Patient()

		patient.pt_id = tpatient
		patient.save()

dataReader = csv.reader(open(csv_filepathname), delimiter = ',', quotechar = '"')

header = dataReader.__next__()
for row in dataReader:
	patient_data = Patient_Data()

	patient_data.lastContact  = row[1]
	patient_data.exp_brca1    = row[2]
	patient_data.exp_usp1     = row[3]
	patient_data.vital_status = row[4]
	patient_data.patient      = Patient.objects.get(pt_id = row[0])

	patient_data.save()
