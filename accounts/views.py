from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

# Create your views here.


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("From is Valid")
            data = form.cleaned_data
            User.objects.create_user(
                username=data["user_name"],
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                password=data["password_2"],
            )
            return redirect("blog:main")
        else:
            # Form is not valid, inspect errors
            print("Form is not valid")
            print(form.errors)  # This will print a dictionary of errors
            # You can also inspect specific fields
            # print(form.errors.get('your_field_name'))
            context = {"form": form}
            return render(request, "register_user.html", context)
    elif request.method == "GET":
        form = UserRegisterForm()
        context = {"form": form}
        return render(request, "register_user.html", context)


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data["user_name"]
            password = form.cleaned_data["password"]
            try:
                user = authenticate(
                    request,
                    username=User.objects.get(email=username_or_email),
                    password=password,
                )
            except:
                user = authenticate(
                    request, username=username_or_email, password=password
                )
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.first_name}!")
                return redirect("blog:main")
            else:
                messages.warning(request, "user name/email or password is invalid!")
                return redirect("accounts:login")

        else:
            # Form is not valid, inspect errors
            print("Form is not valid")
            print(form.errors)  # This will print a dictionary of errors

    elif request.method == "GET":
        form = UserLoginForm()
        context = {"form": form}
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "Successful logout!")
    return redirect("blog:main")
