from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from .forms import *

# Create your views here.
def dashboard(request):
    return render(request, "staff/dashboard.html")

def houses(request):
    form = HouseForm()
    
    if request.method == 'POST':
        # print(f"DATA:::{request.POST}")
        form = HouseForm(request.POST, request.FILES)
        
        if form.is_valid:
            form.save()
            return redirect('customer:index')
    
    context = {
        'form': form
    }
    return render(request, "staff/house_form.html", context)

def locations(request):
    form = LocationForm()
    
    if request.method == "POST":
        form = LocationForm(request.POST)
        
        if form.is_valid:
            form.save()
            form = LocationForm()
            
    context = {
        "form": form,
        "locations": Location.objects.all()
    }
            
    return render(request, "staff/locations.html", context)

def location_houses(request, location_id):
    location = Location.objects.filter(id=location_id).first()
    
    context = {
        "location": location
    }
    
    return render(request, "staff/location_houses.html", context)

def house(request, location_id, house_id):
    house = House.objects.filter(id=house_id).first()
    form = HouseForm(instance=house)
    
    if request.method == "POST":
        print(request.POST)
        
        if dict(request.POST) != model_to_dict(house):
            form = HouseForm(request.POST, request.FILES, instance=house)
            if form.is_valid:
                form.save()
        
    context = {
        "house": house,
        "form": form
    }
    
    return render(request, "staff/house.html", context)