from django import forms
from .models import User,Vaccine,Vaccination
from datetime import date, timedelta
from django import forms
from .models import User, Vaccine

class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nid = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['name', 'address', 'nid']

class VaccinationForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    vaccine = forms.ModelChoiceField(queryset=Vaccine.objects.all())
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['vaccine'].queryset = Vaccine.objects.all()
