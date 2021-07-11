from django.shortcuts import render


def site_login(request):
    context = {}
    return render(request, "user/login.html", context)


def site_register_choice(request):
    context = {}
    return render(request, "user/register_choice.html", context)


def site_register_doctor(request):
    context = {}
    return render(request, "user/register_doctor.html", context)


def site_register_patient(request):
    context = {}
    return render(request, "user/register_patient.html", context)


def site_forgot_password(request):
    context = {}
    return render(request, "user/forgot_password.html", context)
