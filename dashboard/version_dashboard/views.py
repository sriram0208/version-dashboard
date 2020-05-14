from django.http import HttpResponse
from django.shortcuts import render

from .models import Component, ReleaseVersion


def home(request):
    component_list = Component.objects.all()
    release_versions_list = ReleaseVersion.objects.all()
    context = {'component_list': component_list, 'release_versions_list': release_versions_list}
    return render(request, 'home.html', context)