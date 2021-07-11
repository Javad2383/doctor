from django.urls import path
from .views import (site_login, site_register_doctor, site_register_choice, site_register_patient, site_forgot_password)

app_name = "User"
urlpatterns = [
    path('login', site_login, name="login_view"),
    path('register-doctor', site_register_doctor, name="register_doctor"),
    path('register-patient', site_register_patient, name="register_patient"),
    path('register-type', site_register_choice, name="register_type"),
    path('forgot-password', site_forgot_password, name="forgot_password"),
]
