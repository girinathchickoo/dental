from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class PatientData(models.Model):
    
    date=models.DateField(db_column='Date',auto_now_add=True,blank=False)
    mobile_no=models.CharField(max_length=10,primary_key=True,db_column='mobileno',null=False,unique=True)
    first_name=models.CharField(max_length=15,db_column='firstname',null=False)
    last_name=models.CharField(max_length=15,db_column='lastname',null=False)
    age=models.IntegerField(db_column='age',null=False)
    sex=models.CharField(max_length=1,db_column='sex',null=False)
    blood_group=models.CharField(max_length=4,db_column='bloodgroup',null=False)
    chief_complaint=models.TextField(max_length=200,db_column='chief_complaint',null=False)
    medical_history=models.TextField(max_length=200,db_column='medical_history',null=False)
    clinical_findings=models.TextField(max_length=200,db_column='clinical_findings',null=False)
    investigation=models.TextField(max_length=200,db_column='investigation',null=False)
    diagnosis=models.TextField(max_length=200,db_column='diagnosis',null=False)
    prescription=models.TextField(max_length=200,db_column='prescription',null=False)
    next_review_date=models.CharField(max_length=200,db_column='review date',null=False)


def __unicode__ (self):
    return " {0} {1} ".format(self,self.current_date,self.mobile_no)