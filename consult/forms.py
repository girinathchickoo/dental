from django import forms
from .models import PatientData


class DateInput(forms.DateInput):
    input_type='date'

class PatientHistory(forms.Form):
    name=forms.CharField(required=False,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Patient name'}))
    mobile=forms.IntegerField(required=False,label="",widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    fdate=forms.DateField(required=False,label="",widget=DateInput(attrs={'class':'form-control','placeholder':'from date'}))
    tdate=forms.DateField(required=False,label="",widget=DateInput(attrs={'class':'form-control','placeholder':'to date'}))

class ConsultationForm(forms.ModelForm):
    
    class Meta:
        model=PatientData
        fields='__all__'
        labels={"date":"",'mobile_no':"",'first_name':"","last_name":"",'age':"","sex":"","blood_group":"","chief_complaint":"","medical_history":"",'clinical_findings':"","investigation":"","diagnosis":"","prescription":"","next_review_date":""}
        
        widgets={
        'mobile_no':forms.NumberInput(attrs={'class':'form-control','placeholder':'mobile_no'}),
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}),
        'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'Age'}),
        'sex':forms.TextInput(attrs={'class':'form-control','placeholder':'sex'}),
        'blood_group':forms.TextInput(attrs={'class':'form-control','placeholder':'blood group'}),
        'chief_complaint':forms.TextInput(attrs={'class':'form-control','placeholder':'chief complaint'}),
        'medical_history':forms.TextInput(attrs={'class':'form-control','placeholder':'medical history'}),
        'clinical_findings':forms.TextInput(attrs={'class':'form-control','placeholder':'clinical findings'}),
        'investigation':forms.TextInput(attrs={'class':'form-control','placeholder':'investigation'}),
        'diagnosis':forms.TextInput(attrs={'class':'form-control','placeholder':'diagnosis'}),
        'prescription':forms.TextInput(attrs={'class':'form-control','placeholder':'prescription'}),
        'next_review_date':forms.DateInput(attrs={'class':'form-control','placeholder':'review date'}),
        }
        

