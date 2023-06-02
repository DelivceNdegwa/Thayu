from django.urls import path
from .views import *

app_name="customer"
urlpatterns = [
    path('', index, name="index"),
    path('houses/', houses, name="houses"),
    path('properties/', properties, name="properties"),
    path('contact/', contact, name="contact"),
    path('send-message/', send_message, name="send-message")
]
