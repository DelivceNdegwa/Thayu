from django.shortcuts import render, redirect
from django.core.mail import send_mail
from staff.models import *
from .utils import HOUSE_PRICE_RANGE

# Create your views here.
def load_property():
    properties = House.objects.all().order_by('-id')
    
    return properties

def load_locations():
    locations = Location.objects.all()
    return locations

def load_house_types():
    house_types = HouseType.objects.all()
    return house_types

def houses_search(price_range, location_id, house_type_id):
    if price_range == 6:
        return House.objects.filter(
            price__gt=100000,
            location__id=location_id,
            house_type__id=house_type_id
        )
    # i not in the range of 0 to 6, range wont count the last number(7)
    if price_range not in range(7):
        return 

    starting_price = HOUSE_PRICE_RANGE[price_range][0]
    end_price = HOUSE_PRICE_RANGE[price_range][1]
    
    return House.objects.filter(
        price__gte=starting_price, 
        price__lte=end_price,
        location__id=location_id,
        house_type__id=house_type_id
    )
    

def index(request):
    latest_properties = load_property()
    context = {
        "properties": latest_properties,
        "locations": load_locations(),
        "house_types": load_house_types()
    }
    
    return render(request, "customer/index.html", context)

def properties(request):
    context = {
        "properties": House.objects.all()
    }
    return render(request, "customer/property.html", context)

def contact(request):
    return render(request, "customer/contact.html")

def send_message(request):
    message = ""
    if request.method == 'POST':
        message_details_dict = request.POST
        print(f"FIRST NAME= {message_details_dict.get('first-name')}")
        # firstname, lastname, email, phonenumber, message
        firstname = message_details_dict.get('first-name')
        lastname = message_details_dict.get('last-name')
        email = message_details_dict.get('email')
        phonenumber = message_details_dict.get('phone-number')
        message = message_details_dict.get('message')
        
        is_sent = send_email(firstname,lastname, phonenumber,email,message)
        
        if is_sent:
            message = "Email has been sent successfully"
        else:
            message = "Sorry your email was not sent"
              
        context = {
            "is_sent": is_sent,
            "message": message
        }
            
        return render(request, "customer/contact.html", context)
        
    return redirect('customer:contact')

def send_email(firstname, lastname, phonenumber, sender_email, body):
    sent_successfully = False
    email_subject = f'Inquiry from {firstname} {lastname}'
    detailed_body = f'{body} \n \nContact {firstname} through the phone number: {phonenumber}'
    
    try:
        send_mail(
            email_subject,
            detailed_body,
            sender_email,
            ['delivce.ndegwa23@gmail.com'],
            fail_silently=False
        )
        sent_successfully = True
    except Exception as e:
        print("Email was not sent")
        
    return sent_successfully

def property_details(request, property_id):
    property = House.objects.get(id=property_id)
    
    context = {
        "property": property
    }
    
    return render(request, "customer/property_details.html", context)

def house_types(request):
    house_type_list = HouseType.objects.all()
    
    context = {
        "house_types":house_type_list
    }
    
    return render(request, "customer/house.html", context)

def houses_in_category(request, category_id):
    houses = House.objects.filter(house_type__id=category_id).order_by('-id')
    
    context = {
        "properties": houses
    }
    
    return render(request, "customer/houses_in_category.html", context)

def search_results(request):
    search_value = request.GET
    location_id = search_value.get("location")
    house_type_id = search_value.get("house-type")
    house_range = int(search_value.get("budget"))
    
    search_query_results = houses_search(
                                        house_range, 
                                        location_id, 
                                        house_type_id
                                    )
    
    context = {
        "search_results": search_query_results
    }
    
    return render(request, "customer/search_results.html", context)
