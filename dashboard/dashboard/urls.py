from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('versions/', include('version_dashboard.urls')),
    path('environments/', include('environment_dashboard.urls')),
]