from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("User created")
            return redirect("hotels:home")

    form = RegisterForm()
    return render(request, 'account/sign_up.html',
                  {"form":form})