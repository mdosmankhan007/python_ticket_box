from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.crypto import get_random_string
Roles=(('Employee','Employee'),('OILC_Manager','OILC_Manager'),('Deployed_Manager','Deployed_Manager'),('admin','admin'))
class SignUpForm(UserCreationForm):
    role= forms.ChoiceField(choices = Roles)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','role','email']

class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=['Subject','Severity','Type','Report_To','Remarks']

class Comment(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=['Admin_comment']

class Mngr_comment(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=['Mgr_comment']