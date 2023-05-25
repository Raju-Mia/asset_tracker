from django.urls import path
from asset_management import views

# URL Routing for Asset Management apps.
urlpatterns = [
    
    path('companies/', views.CompanyListCreateView.as_view(), name='company-list-create'), # company-list-create url
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'), # employee-list-create url.
    path('devices/', views.DeviceListCreateView.as_view(), name='device-list-create'), # device-list-create url.
    path('logs/', views.DeviceLogListCreateView.as_view(), name='log-list-create'), # log-list-create url.

]
