from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from datetime import date, timedelta
from .forms import UserForm,VaccinationForm
from .models import Vaccine, Vaccination

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def login(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        vaccination_form = VaccinationForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()  # Save the new User entry
            vaccination_date = timezone.now() + timedelta(days=7)
            vaccine_id = vaccination_form.data['vaccine']
            vaccine = Vaccine.objects.get(id=vaccine_id)
            vaccination = Vaccination(user=user, vaccine=vaccine, vaccination_date=vaccination_date)
            vaccination.save()  # Save the new Vaccination entry
            messages.success(request, vaccination_date.strftime("%B %d, %Y"))
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request,"")
            return HttpResponseRedirect(request.path_info) 
    else:
        user_form = UserForm()
        vaccination_form = VaccinationForm()
    
    context = {
        'user_form': user_form,
        'vaccination_form': vaccination_form,
    }

    return render(request, 'login.html', {'user_form': user_form, 'vaccination_form': vaccination_form})

def success(request,context={}):
    return render(request,"success.html",context)