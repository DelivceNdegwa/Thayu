from django.urls import path
from .views import *

app_name="staff"
urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('houses/', houses, name="houses"),
    path('locations/', locations, name="locations"),
    path('locations/houses/<location_id>', location_houses, name="location-houses"),
    path('locations/houses/<location_id>/<house_id>', house, name="house"),
]
