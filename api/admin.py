from django.contrib import admin

# Register your models here.
from .models import Info, Info2

admin.site.register(Info)
admin.site.register(Info2)