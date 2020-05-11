from django.contrib import admin
from .models import Component
from .models import ReleaseVersion
from .models import ServiceVersion

# Register your models here.
admin.site.register(Component)
admin.site.register(ReleaseVersion)
admin.site.register(ServiceVersion)
