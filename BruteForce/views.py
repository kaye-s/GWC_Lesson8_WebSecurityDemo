from django.shortcuts import render, redirect
from .models import Login


def login_view(request):
    error = None

    # Initialize failed attempts list in session
    if "failed_attempts" not in request.session:
        request.session["failed_attempts"] = []

    if request.method == "POST":
        entered_password = request.POST.get("password")

        # check if password exists in DB
        if Login.objects.filter(password=entered_password).exists():
            return redirect("congrats")
        else:
            error = "Incorrect password. Please try again."

            # store failed attempt
            failed_attempts = request.session["failed_attempts"]
            failed_attempts.append(entered_password)
            request.session["failed_attempts"] = failed_attempts
            request.session.modified = True

    return render(request, "login.html", {
        "error": error,
        "failed_attempts": request.session["failed_attempts"]
    })


def congrats_view(request):
    response = render(request, "congrats.html")
    return response

def reset_lab(request):
    request.session.pop("failed_attempts", None)
    return redirect("login")