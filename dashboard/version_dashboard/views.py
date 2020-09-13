import os
import wget
import subprocess
from django.http import HttpResponse
from django.shortcuts import render
from .models import Component, ReleaseVersion, ServiceVersion

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

java_services_pom_urls = {
       
        'service':{
            'dev': '',
            'master': ''
        }
    }

java_services_versions = {}


def home(request):
    component_list = Component.objects.all()
    release_versions_list = ReleaseVersion.objects.all().reverse().order_by('release_name')
    # updateServiceVersion()
    context = {'component_list': component_list, 'release_versions_list': release_versions_list}
    return render(request, 'home.html', context)


def refresh(request):
    return render(request,'login.html')


def login(request):
    if request.POST['login'] == 'admin':
        if request.POST['password'] == 'password':
            getVersionsFromGit()
            updateServiceVersionsInDb()
            return HttpResponse('Updated versions.Go to versions dashboard to view updated versions')
        else:
            return HttpResponse('Invalid credentials!')
    else:
        return HttpResponse('Invalid credentials!')
    return HttpResponse('login success!!')


def getVersionsFromGit():
    for key_components, value_urls in java_services_pom_urls.items():
        print(key_components)
        component_branches = value_urls
        print(value_urls)
        print(component_branches['dev'])
        try:
            file_name = wget.download(component_branches['dev'])
            print(file_name)
            dev_version = subprocess.getoutput("mvn org.apache.maven.plugins:maven-help-plugin:3.1.0:evaluate -Dexpression=project.version -q -DforceStdout")
            dev_version = dev_version.split("-")[0]
            if "ERROR" in dev_version:
                print(dev_version)
                dev_version = ""
            print(dev_version)
            os.remove(os.path.join(BASE_DIR, file_name))
        except:
            print(dev_version)
            dev_version = ""

        try:
            file_name = wget.download(component_branches['master'])
            print(file_name)
            master_version = subprocess.getoutput("mvn org.apache.maven.plugins:maven-help-plugin:3.1.0:evaluate -Dexpression=project.version -q -DforceStdout")
            master_version = master_version.split("-")[0]
            if "ERROR" in master_version:
                print(master_version)
                master_version = ""
            print(master_version)
            os.remove(os.path.join(BASE_DIR, file_name))
        except:
            print(master_version)
            master_version = ""

        temp = {'dev': dev_version, 'master': master_version}

        java_services_versions[key_components] = temp

    print(java_services_versions)


def updateServiceVersionsInDb():
    for key_components, value_versions in java_services_versions.items():
        #update all java components current dev service versions
        current_dev = ReleaseVersion.objects.get(branch='dev')
        updated=ServiceVersion.objects.filter(component__component_name=key_components,release_version__release_name=current_dev.release_name).update(service_version=value_versions['dev'])
        if updated == 0:
            ServiceVersion.objects.create(component=Component(key_components) , release_version=ReleaseVersion(current_dev.release_name), service_version=value_versions['dev'])
        print(updated)

        # update all java components current master service versions
        current_master = ReleaseVersion.objects.get(branch='master')
        updated = ServiceVersion.objects.filter(component__component_name=key_components,release_version__release_name=current_master.release_name).update(service_version=value_versions['master'])
        if updated == 0:
            ServiceVersion.objects.create(component=Component(key_components),release_version=ReleaseVersion(current_master.release_name),service_version=value_versions['master'])
        print(updated)

