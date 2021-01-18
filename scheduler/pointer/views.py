from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, "home.html", {})

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        send_mail(
            name,
            message,
            email,
            ["pablo.iii@outlook.com"],
        )

        return render(request, "contact.html", {"name": name})
    else:
        return render(request, "contact.html", {})
