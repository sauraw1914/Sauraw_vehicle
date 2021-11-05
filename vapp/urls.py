from .views import *
from django.urls import path


urlpatterns =[
     path('',vehicleview,name="vehicleview"),
     path('add',addvehicle,name="addvehicle"),
     path('update',update,name="update"),
     path('list',listvehicle,name="listvehicle"),
     path('updatevehicle/<int:pk>/',updatevehicle,name="updatevehicle"),
     path('deletevehicle/<int:pk>/',deletevehicle,name="deletevehicle"),
]

