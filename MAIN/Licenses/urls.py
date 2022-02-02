from django.urls import path
from . import views


urlpatterns = [
    path('helth_check/', views.health_check),
    path('', views.index),
    path('Licenses/', views.check_lic),
]