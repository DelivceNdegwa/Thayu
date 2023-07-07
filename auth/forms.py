from django.forms import ModelForm

from staff.models import Customer

class CustomerSignUpForm(ModelForm):
    
    class Meta:
        model=Customer
        fields=['first_name', 'last_name', 'email', 'phone', 'national_id_back', 'national_id_front']