from django.contrib import admin

# Register your models here.
from .models import Environments, Services

admin.site.register(Environments)
admin.site.register(Services)

