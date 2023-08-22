from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def login(request):
    form = UserForm()
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect('home')
        else:
            form = UserForm()
    return render(request, 'login.html', {'form': form})
