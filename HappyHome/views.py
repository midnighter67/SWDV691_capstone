from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Provider, SiteUser, Review, Reply, Category, Classification
from .forms import RegisterUserForm, EditProfileForm, UserProfileForm
from django.contrib import messages
import json


"""
  register/login id used as provider_id/user_id, then lookup info with user.id
"""
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
      post = SiteUser()
      if form.is_valid():
         form.save()
         post.first = form.cleaned_data['first_name']
         post.last = form.cleaned_data['last_name']
         post.email = form.cleaned_data['email']
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         user = authenticate(request, username=username, password=password)
         login(request, user)
         messages.success(request, ('Account created'))
         post.ref = request.user
         post.save()
         return redirect('home')
    else:
      form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'create_user.html', context)

def edit_profile_OLD(request):
    if request.user.is_authenticated:
        info = SiteUser.objects.get(ref=request.user)
        form = UserProfileForm(request.POST or None, instance=info)
        if form.is_valid():
            form.save()
            messages.success(request, ('Profile Updated'))
            # return redirect('user_profile')
        else:
            messages.success(request, ('Update Failed'))
    return render(request, 'user_profile.html', {'info': info, 'profile_form': form}) # {'info': info, 'form': form}

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
          form.save()
          update_session_auth_hash(request, form.user) # so updating password doesn't logout user
          messages.success(request, ('Password updated'))
          return redirect('user_profile') # userProfile?
    else:
        form =PasswordChangeForm(user=request.user)
    context = {'password_form': form}
    return render(request, 'user_profile.html', context) # return render(request, 'change_password.html', context)

def search_results(request):
    if request.method == "POST":
        text = request.POST['searchText']
        results = Provider.objects.filter(name__contains=text)
        return render(request, 'results.html', {'results':results})
    else:
        return render(request, 'results.html', {})
    
def user_reviews(request):
    if request.method == "POST":
        mymethod = "post"
    elif request.method == "GET":
        mymethod = "get"
    else:
        mymethod = "neither post nor get"
    return render(request, 'user_reviews.html', {'mymethod':mymethod})


def edit_profile(request):
    if request.user.is_authenticated:
        info = SiteUser.objects.get(ref=request.user)
        profile_form = UserProfileForm(request.POST or None, instance=info)
        password_form = PasswordChangeForm(data=request.POST, user=request.user)
        if request.method == "POST":
            if profile_form in request.POST:
                if profile_form.is_valid():
                    profile_form.save()
                    messages.success(request, ('Profile Updated'))
            if password_form in request.POST:
                if password_form.is_valid():
                    password_form.save()
                    update_session_auth_hash(request, password_form.user) # so updating password doesn't logout user
                    messages.success(request, ('Password updated'))
            # return redirect('user_profile')
        context = {'profile_form':profile_form}
    return render(request, 'user_profile.html', {'info': info, 'profile_form': profile_form})


   
