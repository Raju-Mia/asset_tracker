from rest_framework import serializers
from asset_management.models import Company, Employee, Device, DeviceLog


# ---- ---------------------- Create/Define Serializers -------------------

'''
Create serializers- to convert the model instances to JSON and vice versa.
Define serializers- for each model, specifying the fields to include/exclude.

'''

# For Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
# For Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# For Device
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

# For DeviceLog
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'
