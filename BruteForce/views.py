from django.shortcuts import render, redirect
from .models import Login


def login_view(request):
    error = None

    if request.method == "POST":
        entered_password = request.POST.get("password")

        # check if password exists in DB
        if Login.objects.filter(password=entered_password).exists():
            return redirect("congrats")
        else:
            error = "Incorrect password. Please try again."

    return render(request, "login.html", {"error": error})

def congrats_view(request):
    return render(request, "congrats.html")
