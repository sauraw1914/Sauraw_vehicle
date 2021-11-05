from decimal import Context
from django.shortcuts import render,redirect
from .forms import *
from django.forms import inlineformset_factory

# Create your views here.
def vehicleview(request):
    return render(request,"main.html")



def addvehicle(request):
    form = Vehicle
    if request.method == 'POST':
        form=Vehicle(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])

    context ={'form':form}
    return render(request,"addvehicle.html",context)

def updatevehicle(request,pk):
    vehicle=VehicleModel.objects.get(id=pk)
    form = Vehicle(instance=vehicle)
    if request.method == 'POST':
        form=Vehicle(request.POST,instance=vehicle)
        if form.is_valid():
            form.save()
            vehicles=VehicleModel.objects.all()
            context = {'vehicles':vehicles}
            return render(request,'update.html',context)

    context = {'form':form}
    return render(request,"edit.html",context)

def update(request):
    vehicles=VehicleModel.objects.all()
    context = {'vehicles':vehicles}
    return render(request,"update.html",context)

def listvehicle(request):
    vehicles = VehicleModel.objects.all()
    context ={'vehicles':vehicles}
    return render(request,"list.html",context)

def deletevehicle(request,pk):
    veh =VehicleModel.objects.get(id=pk)
    veh.delete()
    vehicles = VehicleModel.objects.all()
    context ={'vehicles':vehicles}
    return render(request,'list.html',context)