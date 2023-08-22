from django.shortcuts import render
from datetime import date, timedelta
from .forms import UserForm,VaccinationForm

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def login(request):
    if request.method=='POST':
        request.POST = request.POST.copy()
        user_form = UserForm(request.POST)
        request.POST['vaccination_date'] = date.today() + timedelta(days=7)
        vaccination_form = VaccinationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=True)
            print(user)
            print(request.POST)
            # print(vaccination_form.data) # to see the form data
            # print(vaccination_form.errors) # to see the form errors
            # vaccination = vaccination_form.save(commit=False)
            vaccination_form.user = user
            # try:
            #     vaccination_form.is_valid() # to validate the form data
            vaccination_form.save() # to save the form data
            # except ValueError as e:
            #     print(e) # to see the error message
            # redirect('home')
    else:
        user_form = UserForm()
        vaccination_form = VaccinationForm()
    return render(request, 'login.html', {'user_form': user_form, 'vaccination_form': vaccination_form})
