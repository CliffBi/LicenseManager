from django.urls import path
from Licenses import views


urlpatterns = [
    path('', views.index),
    path('get-list/', views.get_list_licenses),
    path('licenses/<data_id>/', views.get_update_delete_license),
    path('licenses/', views.create_licenses),
    # path('licenses/<data_id>/', views.check_licenses),
    # path('licenses/<data_id>/', views.update_licenses),
    # path('licenses/<data_id>/', views.delete_licenses),
]
