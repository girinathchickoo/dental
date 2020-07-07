from django.shortcuts import render,redirect
from .forms import ConsultationForm,PatientHistory
from .models import PatientData
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.models import auth




# Create your views here.
def index(request):
    history=PatientHistory()

    
    if request.method=="POST":
        form=ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            form=ConsultationForm()
            return render(request,'consult.html')
            
    else:
        
        form=ConsultationForm()
    return render(request,"index.html",{"form":form,"history":history})


def fetchpatient(request):
    
    if request.method=='POST':
        history=PatientHistory(request.POST)
        if history.is_valid():
            name=history.cleaned_data.get("name")
            mob=history.cleaned_data.get("mobile")
            s_date=history.cleaned_data.get("fdate")
            e_date=history.cleaned_data.get("tdate")
            mob_no=PatientData.objects.filter(mobile_no=mob)|PatientData.objects.filter(first_name=name)|PatientData.objects.filter(date__range=[s_date,e_date])
            return render(request,"patient.html",{'mob_no':mob_no})
    else:
        history=PatientHistory()
        
    return render(request,"patient.html",{"history":history})


        
    


###class index(TemplateView):
    template_name='index.html'
    def get(self,request):
        form=ConsultationForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=None
        print(request.POST)
        if request.method=='POST' and 'button1' in request.POST:
            form=ConsultationForm(request.POST)
            
            if form.is_valid():
                form.save()
                form=ConsultationForm()
            else:
                form=ConsultationForm()
        else:
            pass
        return render(request,self.template_name,{"form":form})

            


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        
            return render(request,"thanks.html")

        else:
            
            return render(request,"nothanks.html")

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('login')

def home(request):
    
    history=PatientHistory()
    history=PatientHistory()

    
    if request.method=="POST":
        form=ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            form=ConsultationForm()
            return render(request,'consult.html')
            
    else:
        
        form=ConsultationForm()
    return render(request,"index.html",{"form":form,"history":history})

    