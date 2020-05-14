from django.db import models

# Create your models here.


class Environments(models.Model):
    class EnvironmentType(models.TextChoices):
        DEVELOPMENT ='DEV'
        SIT = 'SIT'
        STAGING ='STAG'
        PREPRODUCTION ='PREP'
        PRODUCTION = 'PROD'
        OTHERS = 'OTHERS'
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
        PromotinBroker = "PROMOTION_BROKER"
        CustomerBroker = "CUSTOMER_BROKER"
        PduWrapper = "PDU_WRAPPER"
        NR1Adapter = "NR1_ADAPTER"
        Coupons = "COUPONS"
        Loyalty = "LOYALTY"
        Rewards = "REWARDS"
        PES = "PES"
        IOSever = "IO_SERVER"
        PDU ="PDU"
    environment = models.ForeignKey(Environments, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=30,choices=ServiceName.choices)
    ip_address = models.GenericIPAddressField(null=True,blank=True)
    health_endpoint = models.CharField(max_length=200,blank=True)
    additional_details = models.TextField(max_length=1000,blank=True)

    class Meta:
        unique_together = ('environment', 'service_name')

    def __str__(self):
        return "%s : %s" %(self.environment,self.service_name)



