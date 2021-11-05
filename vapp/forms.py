from django import forms
from django.db.models import fields
from django.forms import ModelForm,widgets
from django.utils.safestring import mark_safe


from .models import *

class Vehicle(ModelForm):
    class Meta:
        model = VehicleModel
        fields='__all__'
        labels ={
            'name':'',
            'camera1':'',
            'camera2':'',
            'staticmap':'',
            'speed':'',
            'avgspeed':'',
            'temperature':'',
            'energystatus':'',
            'fuellevel':''


        }
        
        widgets = {
            'name': forms.TextInput( attrs ={'class': 'field','placeholder':'Vehicle name'}),
            'camera1': forms.TextInput(attrs ={'class': 'field','placeholder':'Camera 1'}),
            'camera2': forms.TextInput(attrs ={'class': 'field','placeholder':'Camera 2'}),
            'staticmap': forms.TextInput(attrs ={'class': 'field','placeholder':'Static Map'}),
            'speed': forms.TextInput(attrs ={'class': 'field','placeholder':'Speed'}),
            'avgspeed': forms.TextInput(attrs ={'class': 'field','placeholder':'Average Speed'}),
            'temperature': forms.TextInput(attrs ={'class': 'field','placeholder':'Temperature'}),
            'energystatus': forms.TextInput(attrs ={'class': 'field','placeholder':'Energy Status'}),
            'fuellevel': forms.TextInput(attrs ={'class': 'field','placeholder':'Fuel Level'}),

        }