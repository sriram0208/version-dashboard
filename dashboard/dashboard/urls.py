from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('versions/', include('version_dashboard.urls')),
    path('admin/', admin.site.urls),
]