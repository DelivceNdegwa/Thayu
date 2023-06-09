from django.urls import path
from .views import *

app_name="staff"
urlpatterns = [
    path('', dashboard, name="dashboard")
]
