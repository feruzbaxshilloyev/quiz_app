from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404

from app.models import Test, Baza
from .forms import CustomUserForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm


def profil_view(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    foiz = round((user.true_quiz / user.total_quiz) * 100, 2) if user.total_quiz else 0
    return render(request, 'profil.html', {'user': user, 'foiz': foiz})


def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profil:profil')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'edit_profil.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Ro‘yxatdan muvaffaqiyatli o‘tdingiz!")
            return redirect('profil:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('app:home')
        else:
            return redirect('app:home')
    return render(request, 'login.html')


# Logout view
def logout_view(request):
    auth_logout(request)
    return redirect('app:home')


def my_tests(request):
    bazas = Baza.objects.filter(author=request.user)
    return render(request, 'my_tests.html', {'bazas': bazas})


def delete_test(request, id):
    test = get_object_or_404(Test, id=id, baza__author=request.user)
    test.delete()
    return redirect('profil:my_tests')
