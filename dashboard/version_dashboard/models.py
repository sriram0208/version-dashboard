from django.db import models


class Component(models.Model):
    component_name = models.CharField(max_length=50)

    def __str__(self):
        return self.component_name


class ReleaseVersion(models.Model):
    release_name = models.CharField(max_length=6)

    def __str__(self):
        return self.release_name


class ServiceVersion(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    release_version = models.ForeignKey(ReleaseVersion, on_delete=models.CASCADE)
    service_version = models.CharField(max_length=6)
    def __str__(self):
        return "%s %s" %(self.component ,self.service_version)
