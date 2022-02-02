from django.urls import path
from Licenses import views


urlpatterns = [
    path('helth_check/', views.get_list_licenses),
    path('', views.index),
    path('licenses/<id>/', views.check_lic),
]