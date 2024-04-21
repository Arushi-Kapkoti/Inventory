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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django_pandas.io import read_frame
import plotly
import plotly.express as px

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

class StockList(LoginRequiredMixin,ListView):
    model = Inventory
    template_name = 'main/dashboard.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user)
        context['count'] = context['items'].count() 
        #context['market_count'] = context['items'].filter(sale_status='on_sale')
        return context

class ItemDetail(LoginRequiredMixin,DetailView):
    model = Inventory
    template_name = 'main/item_detail.html'
    context_object_name = 'item'

class CreateItem(LoginRequiredMixin, CreateView):
    model = Inventory
    template_name = 'main/create_item_form.html'
    fields = ['name', 'item_type', 'cost_per_item', 'quantity_in_stock', 'quantity_sold', 'sale_status', 'item_image']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Set last_sales_date if quantity_sold is provided
        quantity_sold = form.cleaned_data['quantity_sold']
        if quantity_sold is not None:
            form.instance.last_sales_date = timezone.now().date()

            # Calculate sales
            cost_per_item = form.cleaned_data['cost_per_item']
            form.instance.sales = quantity_sold * cost_per_item

        return super().form_valid(form)

class UpdateItem(LoginRequiredMixin,UpdateView):
    model = Inventory
    fields = ['name', 'item_type', 'cost_per_item', 'quantity_in_stock', 'quantity_sold']
    template_name = 'main/create_item_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        # Get the instance of the object being updated
        instance = form.instance
        
        # Check if quantity_sold has changed
        if form.cleaned_data['quantity_sold'] != instance.quantity_sold:
            # If quantity_sold has changed, update last_sales_date to current date
            instance.last_sales_date = timezone.now()

        # Calculate sales if quantity_sold is updated
        quantity_sold = form.cleaned_data['quantity_sold']
        cost_per_item = instance.cost_per_item  # Use instance's current cost_per_item
        if quantity_sold is not None:
            instance.sales = quantity_sold * cost_per_item

        return super().form_valid(form)

class DeleteItem(LoginRequiredMixin,DeleteView):
    model = Inventory
    context_object_name = 'item'
    template_name = 'main/item_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

@login_required
def analytics(request):
    inventories = Inventory.objects.all()
    df = read_frame(inventories)


def marketPlace(request):
    return HttpResponse('MarketPlace')
