from django import forms
from .models import User,Vaccine

# class VaccineForm(forms.ModelForm):
#     class Meta:
#         model = Vaccine
#         fields = ['vaccine_name']

class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nid = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    vaccine = forms.ModelChoiceField(queryset=Vaccine.objects.all().order_by('vaccine_name'), widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = User
        fields = ['name', 'address', 'nid']
