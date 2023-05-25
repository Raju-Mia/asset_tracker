from django.db import models

# Create your models here.


# ----- Define the Models For Asset Tracker Management System -----

'''

Define the models.
Include the necessary fields, relationships, and any additional methods or meta options.

'''
# Company Model
class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Employee Model
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees') # many-to-one relationship between- company Model.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Device Model
class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='devices') # many-to-one relationship between- company Model.
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# DeviceLog Model
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='logs') # many-to-one relationship between- Device Model.
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) # many-to-one relationship between- Employee Model.
    
    checked_out = models.DateTimeField()
    returned = models.DateTimeField(null=True)
    condition_at_checkout = models.CharField(max_length=255)
    condition_at_return = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.device.name} - {self.employee.name}"

