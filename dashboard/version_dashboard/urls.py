from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('refresh/',views.refresh, name='refresh'),
    path('refresh/status',views.login, name='login'),
]