

from django.urls import path, include
from Licenses import views


urlpatterns = [
    path('', views.GetCreateUpdateDelete.index, name="index"),
    path('get-list/', views.GetCreateUpdateDelete.get_list_licenses, name='get-list'),
    path('license/<data_id>/', views.GetCreateUpdateDelete.get_update_delete_license, name='get_license'),
    path('v2/licenses/<int:pk>', views.DrfGetUpdateCreateDelete.GetUpdateDeleteLicense.as_view(), name='v2_license_id'),
    path('license/', views.GetCreateUpdateDelete.create_licenses, name='license'),
    path('v2/license/', views.DrfGetUpdateCreateDelete.CreateLicense.as_view(), name='v2_license'),
    # path('licenses/<data_id>/', views.check_licenses),
    # path('licenses/<data_id>/', views.update_licenses),
    # path('licenses/<data_id>/', views.delete_licenses),
]
