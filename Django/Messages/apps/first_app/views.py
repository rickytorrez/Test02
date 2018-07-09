from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, "first_app/index.html")

def register(request):
    response = User.objects.register(
        request.POST["first"],
        request.POST["last"],
        request.POST["username"],
        request.POST["email"],
        request.POST["dob"],
        request.POST["password"],
        request.POST["confirm"]
    )

    if response["valid"]:
        request.session["user_id"] = response["user"].id
        return redirect("/dashboard")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")

def login(request):
    response = User.objects.login(
        request.POST["email"],
        request.POST["password"]
    )
    if response["valid"]:
        request.session["user_id"] = response["user"].id
        return redirect("/dashboard")
    else:
        for error_message in response["errors"]:
            messages.add_message(request, messages.ERROR, error_message)
        return redirect("/")

def dashboard(request):
    if "user_id" not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session["user_id"])
    return render(request, "first_app/dashboard.html", {"user":user})

def logout(request):
    request.session.clear()
    return redirect("/")