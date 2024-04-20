from django.urls import path
from . import views

urlpatterns = [
    path('',views.marketPlace, name = 'market-place'),
    path('register/',views.SignUpView.as_view(), name = 'register'),
    path('login/',views.UserLoginPageView.as_view(), name = 'login'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
]