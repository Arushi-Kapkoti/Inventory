from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from main.models import CustomUser, Inventory
from main.form import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout as logouts

from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'

class UserLoginPageView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

def logoutUser(request):
    if request.method=='GET':
        logouts(request)
        return redirect('login')

class StockList(ListView):
    model = Inventory
    template_name = 'main/dashboard.html'
    context_object_name = 'items'

class ItemDetail(DetailView):
    model = Inventory
    template_name = 'main/item_detail.html'
    context_object_name = 'item'

class CreateItem(CreateView):
    model = Inventory
    template_name = 'main/create_item_form.html'
    fields = '__all__'
    success_url = reverse_lazy('dashboard')

class UpdateItem(UpdateView):
    model = Inventory
    fields = '__all__'
    template_name = 'main/create_item_form.html'
    success_url = reverse_lazy('dashboard')

class DeleteItem(DeleteView):
    model = Inventory
    context_object_name = 'item'
    template_name = 'main/item_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

def marketPlace(request):
    return HttpResponse('MarketPlace')

# def dashboard(request):
#     return HttpResponse('Dashboard')
