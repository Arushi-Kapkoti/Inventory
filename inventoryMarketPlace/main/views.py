from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from main.models import CustomUser
from main.form import CustomUserCreationForm
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'

class UserLoginPageView(LoginView):
    template_name = 'main/login.html'

def marketPlace(request):
    return HttpResponse('MarketPlace')

def dashboard(request):
    return HttpResponse('Dashboard')