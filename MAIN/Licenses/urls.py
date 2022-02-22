from django.urls import path
from Licenses import views, viewsDRF
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'v3/license', viewsDRF.LicenseViewSet, basename='user')


urlpatterns = [
    path('', views.index, name="index"),
    path('get-list/', views.get_list_licenses, name='get-list'),
    path('license/<data_id>/', views.get_update_delete_license, name='get_license'),
    path('license/', views.create_licenses, name='license'),
    path('test_license/', views.license_comparison, name='license_comparison'),
    path('v2/license/<int:pk>', viewsDRF.GetUpdateDeleteLicense.as_view(), name='v2_license_id'),
    path('v2/license/', viewsDRF.CreateLicense.as_view(), name='v2_license'),
    # path('v3/licenses/<int:pk>', viewsDRF.GetUpdateDeleteLicense.as_view(), name='v3_license_id'),
    # path('v3/license/', viewsDRF.CreateLicense.as_view(), name='v3_license'),
    # path('v3/license/', viewsDRF.LicenseView.as_view({'get': 'list'})),
    # path('v3/license/<int:pk>', viewsDRF.LicenseViewSet.as_view({'get': 'retrieve'})),
]

urlpatterns += router.urls
