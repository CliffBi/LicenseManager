from django.urls import path
from Licenses import views


urlpatterns = [
    path('', views.index),
    path('get-list/', views.get_list_licenses),
    path('licenses/<data_id>/', views.check_lic),
    path('data-updater/<data_id>/', views.data_updater),
    path('data-create/', views.data_create),
    path('data-delete/<data_id>/', views.data_delete),
]