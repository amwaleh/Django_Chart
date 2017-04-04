from django.contrib import admin
from .models import Country, Population
# Register your models here.
admin.site.register([Country,Population])