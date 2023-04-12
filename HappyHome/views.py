from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Provider, User, Review, Reply, Category, Classification
from .forms import RegisterUserForm, EditProfileForm
from django.contrib import messages
import json



# views
def home(request):
    if request.method == 'GET':
        message = "Hello World"
    else:
        message = "Hello World!"
    return render(request, 'home.html', {'message':message})


    
def login_user(request):
    if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        messages.success(request, ('You have been logged in'))
        return redirect('home')
      else:
        messages.success(request, ('Error logging in'))
        return redirect('login')
    else:
      return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
      form = RegisterUserForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         user = authenticate(request, username=username, password=password)
         login(request, user)
         messages.success(request, ('Account created'))
         return redirect('home')
    else:
      form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'create_user.html', context)

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
          form.save()
          messages.success(request, ('Profile updated'))
          return redirect('user_profile')
    else:
        form =EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'user_profile.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
          form.save()
          update_session_auth_hash(request, form.user) # so updating password doesn't logout user
          messages.success(request, ('Password updated'))
          return redirect('user_profile')
    else:
        form =PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'change_password.html', context)

def search_results(request):
    if request.method == "POST":
        text = request.POST['searchText']
        results = Provider.objects.filter(name__contains=text)
        return render(request, 'results.html', {'results':results})
    else:
        return render(request, 'results.html', {})