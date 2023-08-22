from django import forms
from .models import User,Vaccine,Vaccination
from datetime import date, timedelta

# class VaccineForm(forms.ModelForm):
#     class Meta:
#         model = Vaccine
#         fields = ['vaccine_name']

class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nid = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['name', 'address', 'nid']

class VaccinationForm(forms.ModelForm):
    vaccine = forms.ModelChoiceField(queryset=Vaccine.objects.all().order_by('vaccine_name'), widget=forms.Select(attrs={'class': 'form-select'}))
    # vaccination_date = forms.DateField(initial=date.today() + timedelta(days=7), input_formats=['%m-%d-%Y'])
    class Meta:
        model = Vaccination
        fields = ("user","vaccine","vaccination_date")

