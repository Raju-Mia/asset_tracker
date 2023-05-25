from django.shortcuts import render
from rest_framework import generics
from asset_management.models import Company, Employee, Device, DeviceLog
from asset_management.serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer


# ---------- Implement Views for Asset Management App -----------------

'''

In the app's views.py file, created views that handle the different API endpoints.
Use Django REST Framework's generic views for common operations such as list, create, retrieve, update, and delete.

'''


# CompanyListCreate View 
class CompanyListCreateView(generics.ListCreateAPIView): 
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# EmployeeListCreate View
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# DeviceListCreate View
class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

# DeviceLogListCreate View
class DeviceLogListCreateView(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

