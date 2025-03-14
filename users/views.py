from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .form import UserRegisterForm

# Create your views here.

def register(request, *args, **kwargs):
    print(args, kwargs)
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('homepage')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form':form})