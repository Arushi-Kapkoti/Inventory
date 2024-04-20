from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.form import CustomUserCreationForm, CustomUserChangeForm
from main.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser,CustomUserAdmin)