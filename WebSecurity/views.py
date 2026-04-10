from django.shortcuts import render, redirect
from .models import Login
from django.http import JsonResponse


def home_view(request):
    return render(request, "index.html")

def amaze_view(request):
    return render(request, "amaze.html")

def barbie_flag(request):
    return JsonResponse({"flag": "flag_barbie{bA==}"})

def barbie_view(request):
    return render(request, "barbie.html")

def notebook_view(request):
    return render(request, "notebook.html")

def fallguy_view(request):
    flag = None

    if request.method == "POST":
        user_input = request.POST.get("secrettext", "").lower().strip()

        # correct answer based on your hint
        if user_input == "colt":  # Ryan Gosling's character in The Fall Guy
            flag = "flag-fallguy{YQ==}"

    return render(request, "fallguy.html", {"flag": flag})

def login_view(request):
    context = {}

    # hardcoded creds for demo
    correct_email = "bob.manager@email.com"
    sqlinjection = "'OR '1'='1 --"
    correct_password = "Ryang0sling"

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email == sqlinjection:
            context["flag"] = "Congrats! You gained unauthorized access to this login page via SQL Injection. That's pretty neat."
        elif email == correct_email and password == correct_password:
            context["flag"] = "flag-login{cg==}"
        elif email != correct_email and password != correct_password:
            context["error"] = "Incorrect email and password"
        elif email != correct_email:
            context["error"] = "Incorrect email"
        elif password != correct_password:
            context["error"] = "Incorrect password"

    return render(request, "login.html", context)

def lala_view(request):
    return render(request, "lala.html")

def submit_view(request):
    context = {}

    if request.method == "POST":
        user_input = request.POST.get("secrettext", "").lower().strip()

        if user_input == "hailmary":
            context["flag"] = "FLAG{final_message_here}"
            return render(request, "challenge.html", context)
        else:
            context["error"] = "Incorrect answer. Try again."

    return render(request, "submit.html", context)

def challenge_view(request):
    return render(request, "challenge.html")
