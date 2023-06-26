from django import forms
from django.forms import ModelForm
from staff.models import *


class HouseForm(ModelForm):
    class Meta:
        model=House
        fields= '__all__'  #['name', 'location']
        

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        
        
class LocationForm(ModelForm):
    class Meta:
        model=Location
        fields='__all__'
        

class HouseTypeForm(ModelForm):
    class Meta:
        model=HouseType
        fields='__all__'
        

class AmenitiesForm(ModelForm):
    class Meta:
        model=Amenities
        fields='__all__'
        

        
    