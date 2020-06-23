from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Environments,Services


def index(request):
    environments_list = Environments.objects.all()
    environment_types_list=Environments.EnvironmentType.values
    context={'environments_list':environments_list,'environment_types_list':environment_types_list}
    return render(request,"index.html",context)

def detail(request,environment_name):
    environment = Environments.objects.get(pk=environment_name)
    environments_list = Environments.objects.all()
    environment_types_list=Environments.EnvironmentType.values
    context = {'environment':environment,'environments_list':environments_list,'environment_types_list':environment_types_list}
    return render(request,"detail.html",context)
