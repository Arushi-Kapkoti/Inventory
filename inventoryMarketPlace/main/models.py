from django.db import models
#importing AbstractUser class so that we can inherit from it
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    STATES = {
        "Andaman and Nicobar Islands": "Andaman and Nicobar Islands",
        "Andhra Pradesh": "Andhra Pradesh",
        "Arunachal Pradesh": "Arunachal Pradesh",
        "Assam": "Assam",
        "Bihar": "Bihar",
        "Chandigarh": "Chandigarh",
        "Chhatisgarh": "Chhatisgarh",
        "Dadra and Nagar Haveli and Daman & Diu":"Dadra and Nagar Haveli and Daman & Diu",
        "Delhi NCT":"Delhi NCT",
        "Goa": "Goa",
        "Haryana": "Haryana",
        "Himachal Pradesh": "Himachal Pradesh",
        "Jammu and Kashmir": "Jammu and Kashmir",
        "Jharkhand": "Jharkhand",
        "Karnatka": "Karnatka",
        "Kerala": "Kerala",
        "Ladakh": "Ladhakh",
        "Lakshadweep":"Lakshadweep",
        "Madhya Pradesh": "Madhya Pradesh",
        "Maharashtra": "Maharashtra",
        "Manipur": "Manipur",
        "Meghalaya": "Meghalaya",
        "Mizoram": "Mizoram",
        "Nagaland": "Nagaland",
        "Odisha": "Odisha",
        "Puducherry": "Puducherry",
        "Punjab": "Punjab",
        "Rajasthan": "Rajasthan",
        "Sikkim": "Sikkim",
        "Tamil Nadu": "Tamil Nadu",
        "Telangana": "Telengana",
        "Tripura": "Tripura",
        "Uttarakhand": "Uttarakhand",
        "Uttar Pradesh": "Uttar Pradesh",
        "West Bengal": "West Bengal"
    }
    aadhar = models.PositiveIntegerField(null = True, blank = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=40, choices = STATES)
    phone_number = models.PositiveIntegerField(null = True, blank = True)

# class Inventory(models.Model):
#     name = models.CharField(max_length=100,null = False, blank = False)
#     cost_per_item = models.DecimalField(max_digits=19,decimal_places=2,null = False, blank = False)
#     quantity_in_stock = models.IntegerField(null = False, blank = False)
#     quantity_sold = models.IntegerField(null = True, blank = True)
#     sales = models.DecimalField(max_digits=19,decimal_places=2, null = True, blank = True)
#     stock_date = models.DateField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.name