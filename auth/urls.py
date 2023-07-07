from django.urls import path

from .views import *

urlpatterns = [
    path('customer/register', customer_signup, name="customer-signup"),
    path('user/logout', signout, name="signout")
]
