from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

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

def blog_sigle(request):
    return render(request, "blog-single.html", {})

def blog(request):
    return render(request, "blog.html", {})

def department(request):
    return render(request, "department.html", {})

def doctor(request):
    return render(request, "doctor.html", {})

def pricing(request):
    return render(request, "pricing.html", {})

def appointment(request):
    if request.method == "POST":
        your_name = request.POST["your_name"]
        pro_name = request.POST["pro_name"]
        email = request.POST["pro_name"]
        # department = request.POST["department"]
        date = request.POST["date"]
        time = request.POST["time"]       

        appointment = "Name: " + your_name + "\nProfissonal: " + pro_name + "\nDay: " + date + "\nHour: " + time

        send_mail(
            "Appointment Request",
            appointment,
            email,
            ["pablo.iii@outlook.com"],
        )
        return render(request, "appointment.html", {"your_name": your_name, "pro_name": pro_name, "date": date, "time": time})
    else:
        return render(request, "home.html", {})
    

