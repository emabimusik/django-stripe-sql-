from django.contrib import admin

from .models import FitnessPlan
from .models import Customer

admin.site.register(FitnessPlan)

admin.site.register(Customer)

