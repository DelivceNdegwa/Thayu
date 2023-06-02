from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def load_property():
    properties = [
        {
            "name": "Tokas PentHouse",
            "image_url": "https://images.unsplash.com/photo-1595243643203-06ba168495ea?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=435&q=80"
        },
        {
            "name": "Muthungu TreeHouse",
            "image_url": "https://images.unsplash.com/photo-1550355191-aa8a80b41353?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=987&q=80"
        },
        {
            "name": "Amani Cottage",
            "image_url": "https://images.unsplash.com/photo-1568605114967-8130f3a36994?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80"
        },
        {
            "name": "Amani Cottage 2",
            "image_url": "https://images.unsplash.com/photo-1568605114967-8130f3a36994?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80"
        },
    ]
    
    return properties

def load_locations():
    locations = ['Kenya','Tanzania', 'Ethopia', 'Uganda']
    return locations

def index(request):
    
    context = {
        "properties": load_property(),
        "locations": load_locations()
    }
    
    return render(request, "customer/index.html", context)


def houses(request):
    return render(request, "customer/house.html")

def properties(request):
    return render(request, "customer/property.html")

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
