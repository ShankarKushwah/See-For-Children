from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from accounts.forms import NGOForm, SignUpForm


def register(request):
    if request.method == 'POST':
        form = NGOForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return render('saved')
    else:
        form = NGOForm()
    return render(request, 'accounts/registration.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/register/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
