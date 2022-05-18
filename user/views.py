from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, UserProfileForm




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #user = authenticate(username=username, password=password)
            messages.success(request, ("Enregistré avec succès, vous pouvez se connecter après l'autorisation de l'administrateur..."))
            return redirect('login')
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()

    return render(request, 'authenticate/register.html', {
        'form':form,
        'profile_form':profile_form,
        
    })



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.userprofile.Is_approved :
            login(request, user)
            return redirect('product:home')
        else:
            messages.success(request, ("SVP, veuillez attendre l'autorisation de l'administrateur"))
            return redirect('login')


    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("vous étiez déconnecté"))
    return redirect('product:home')







