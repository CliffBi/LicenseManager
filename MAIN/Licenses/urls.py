from django.urls import path
from Licenses import views


urlpatterns = [
    path('', views.GetCreateUpdateDelete.index),
    path('get-list/', views.GetCreateUpdateDelete.get_list_licenses),
    path('licenses/<data_id>/', views.GetCreateUpdateDelete.get_update_delete_license),
    path('v2/licenses/<int:pk>', views.DrfGetUpdateCreateDelete.GetUpdateDeleteLicense.as_view()),
    path('licenses/', views.GetCreateUpdateDelete.create_licenses),
    path('v2/licenses/', views.DrfGetUpdateCreateDelete.CreateLicense.as_view()),
    # path('licenses/<data_id>/', views.check_licenses),
    # path('licenses/<data_id>/', views.update_licenses),
    # path('licenses/<data_id>/', views.delete_licenses),
]
