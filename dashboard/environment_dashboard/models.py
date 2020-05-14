from django.db import models

# Create your models here.


class Environments(models.Model):
    class EnvironmentType(models.TextChoices):
        DEVELOPMENT ='DEV'
        SIT = 'SIT'
        STAGING ='STAG'
        PREPRODUCTION ='PREP'
        PRODUCTION = 'PROD'
    environment_name = models.CharField(max_length=50,null=False,primary_key=True)
    environment_type = models.CharField(max_length=10,choices=EnvironmentType.choices,blank=True)

    def __str__(self):
        return self.environment_name


class Services(models.Model):
    class ServiceName(models.TextChoices):
        Logix = 'LOGIX'
        EPM = 'EPM'
        OCD = 'OCD'
        Messaging = 'MESSAGING'
    environment = models.ForeignKey(Environments, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=20,choices=ServiceName.choices)
    ip_address = models.GenericIPAddressField(null=True,blank=True)
    health_endpoint = models.CharField(max_length=50,blank=True)
    remarks = models.TextField(max_length=100,blank=True)

    class Meta:
        unique_together = ('environment', 'service_name')

    def __str__(self):
        return "%s : %s" %(self.environment,self.service_name)
